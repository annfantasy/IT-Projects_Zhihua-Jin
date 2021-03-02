<template>
  <div v-loading="loading" class="health">
    <mu-appbar style="width: 100%;" title="Health" color="primary"/>
    <mu-flex justify-content="center" align-items="center">
      <mu-button full-width color="success" class="health-questionnaire" @click="$router.push('/questionnaire')">My Questionnaire</mu-button>
    </mu-flex>
    <mu-container class="health-appointment">
      <mu-paper :z-depth="1">
        <mu-list v-if="account.role === 0" textline="three-line">
          <mu-sub-header>My Appointment</mu-sub-header>
          <div v-for="(appointment, index) in appointmentList" :key="index" @click="openAppointment(appointment)">
            <mu-list-item avatar button>
              <mu-list-item-action>
                <mu-avatar>
                  <img src="@/assets/image/demo/avatar.png">
                </mu-avatar>
              </mu-list-item-action>
              <mu-list-item-content>
                <mu-list-item-title>{{ appointment.doctor.name }}</mu-list-item-title>
                <mu-list-item-sub-title>
                  <span style="color: rgba(0, 0, 0, .87)">{{ appointment.doctor.doctor.introduction }}</span><br>
                  {{ appointment.date.split('T')[0] }}
                </mu-list-item-sub-title>
              </mu-list-item-content>
              <mu-list-item-action v-if="appointment.status === 0">
                <mu-icon value="arrow_forward"/>
              </mu-list-item-action>
              <mu-list-item-action v-else-if="appointment.status === 1">
                <mu-icon value="check"/>
              </mu-list-item-action>
              <mu-list-item-action v-else-if="appointment.status === 2">
                <mu-icon value="close"/>
              </mu-list-item-action>
              <mu-list-item-action v-else>
                <mu-icon value="cancel"/>
              </mu-list-item-action>
            </mu-list-item>
            <mu-divider/>
          </div>
        </mu-list>
      </mu-paper>
    </mu-container>

    <mu-container class="health-doctor">
      <mu-paper :z-depth="1">
        <mu-list v-if="account.role === 0" textline="three-line">
          <mu-sub-header>Available Doctor</mu-sub-header>
          <div v-for="(doctor, index) in doctorList" :key="index" @click="openSchedule(doctor.id)">
            <mu-list-item avatar button>
              <mu-list-item-action>
                <mu-avatar>
                  <img src="@/assets/image/demo/avatar.png">
                </mu-avatar>
              </mu-list-item-action>
              <mu-list-item-content>
                <mu-list-item-title>{{ doctor.name }}</mu-list-item-title>
                <mu-list-item-sub-title>
                  <span style="color: rgba(0, 0, 0, .87)">{{ doctor.doctor.organization }}</span><br>
                  {{ doctor.doctor.introduction }}
                </mu-list-item-sub-title>
              </mu-list-item-content>
              <mu-list-item-action>
                <mu-icon value="chat_bubble"/>
              </mu-list-item-action>
            </mu-list-item>
            <mu-divider/>
          </div>
        </mu-list>
      </mu-paper>
    </mu-container>
    <mu-dialog :open.sync="openMyAppointment" title="My Appointment">
      <mu-date-input
        v-model="appointment.date"
        :date-time-format="enDateFormat"
        icon="today"
        label="Date"
        container="dialog"
        disabled
        label-float
        full-width/>
      <mu-date-input
        v-model="appointment.time"
        icon="today"
        label="Time"
        container="dialog"
        type="time"
        disabled
        label-float
        full-width/>
      <mu-text-field v-model="appointment.content" :rows="4" disabled multi-line full-width/>
      <mu-button slot="actions" flat color="primary" @click="cancelAppointment">Cancel</mu-button>
    </mu-dialog>
    <mu-dialog :open.sync="openPostAppointment" title="Make Appointment">
      <mu-date-input
        v-model="appointmentForm.date"
        :date-time-format="enDateFormat"
        icon="today"
        label="Choose date"
        container="dialog"
        label-float
        full-width/>
      <mu-date-input
        v-model="appointmentForm.time"
        icon="today"
        label="Choose time"
        container="dialog"
        type="time"
        label-float
        full-width/>
      <mu-text-field v-model="appointmentForm.content" :rows="4" multi-line full-width/>
      <mu-button slot="actions" flat color="primary" @click="submitAppointment">Submit</mu-button>
    </mu-dialog>
  </div>
</template>

<script>
import Toast from 'muse-ui-toast'
import { mapGetters } from 'vuex'
import { getDoctorList } from '@/api/doctor'
import { postAppointment, getAppointmentByPatientId, updateAppointmentStatus } from '@/api/appointment'

const dayAbbreviation = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
const dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
const monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
  'Oct', 'Nov', 'Dec']
const monthLongList = ['January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December']

const enDateFormat = {
  formatDisplay(date) {
    return `${dayList[date.getDay()]}, ${monthList[date.getMonth()]} ${date.getDate()}`
  },
  formatMonth(date) {
    return `${monthLongList[date.getMonth()]} ${date.getFullYear()}`
  },
  getWeekDayArray(firstDayOfWeek) {
    const beforeArray = []
    const afterArray = []
    for (let i = 0; i < dayAbbreviation.length; i++) {
      if (i < firstDayOfWeek) {
        afterArray.push(dayAbbreviation[i])
      } else {
        beforeArray.push(dayAbbreviation[i])
      }
    }
    return beforeArray.concat(afterArray)
  },
  getMonthList() {
    return monthList
  }
}

export default {
  name: 'Health',
  data() {
    return {
      doctorList: [],
      appointmentList: [],
      openMyAppointment: false,
      openPostAppointment: false,
      appointment: {},
      appointmentForm: {
        patientId: undefined,
        doctorId: undefined,
        date: undefined,
        time: undefined,
        content: ''
      },
      enDateFormat,
      loading: true
    }
  },
  computed: {
    ...mapGetters([
      'account'
    ])
  },
  mounted() {
    this.appointmentForm.patientId = this.account.id
    const that = this
    getDoctorList().then((response) => {
      if (response.code === 200) {
        that.doctorList = response.data
      }
    }).catch(() => {
      Toast.error('Failed loading doctor list.')
    })
    getAppointmentByPatientId(this.account.id).then((response) => {
      if (response.code === 200) {
        that.appointmentList = response.data
        this.loading = false
      }
    }).catch(() => {
      Toast.error('Failed loading appointment list.')
      this.loading = false
    })
  },
  methods: {
    openSchedule(doctorId) {
      this.appointmentForm.doctorId = doctorId
      this.openPostAppointment = true
    },
    openAppointment(appointment) {
      this.appointment = appointment
      this.openMyAppointment = true
    },
    submitAppointment() {
      const that = this
      if (this.appointmentForm.doctorId === undefined || this.appointmentForm.date === undefined || this.appointmentForm.time === undefined) {
        Toast.error('Please choose the schedule.')
      } else {
        postAppointment(this.appointmentForm).then(response => {
          if (response.code === 200) {
            that.appointmentList.push(response.data)
            that.appointmentForm = {
              patientId: that.account.id,
              doctorId: undefined,
              date: undefined,
              time: undefined,
              content: ''
            }
          }
          Toast.success('Create appointment successfully.')
          this.openPostAppointment = false
        }).catch(() => {
          this.loading = false
        })
      }
    },
    cancelAppointment() {
      updateAppointmentStatus(this.appointment.id, 4).then((response) => {
        if (response.code === 200) {
          this.appointment.status = 4
          Toast.success('Appointment canceled.')
          this.openMyAppointment = false
        }
      }).catch(() => {
        Toast.error('Failed canceling appointment.')
        this.openMyAppointment = false
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .health {
    &-questionnaire {
      margin-top: 1.3rem;
      margin-bottom: 1.3rem;
    }

    &-appointment {
      width: 100%;
      overflow: hidden;
      margin-bottom: 1.3rem;
    }

    &-doctor {
      margin-top: 1.3rem;
      width: 100%;
      overflow: hidden;
      margin-bottom: 1.3rem;
    }
  }
</style>
