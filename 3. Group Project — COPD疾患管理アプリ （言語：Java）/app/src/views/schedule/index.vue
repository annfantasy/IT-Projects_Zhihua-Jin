<template>
  <div v-loading="loading" class="schedule">
    <mu-appbar style="width: 100%;" title="Schedule" color="primary"/>
    <mu-container class="schedule-appointment">
      <mu-paper :z-depth="1">
        <mu-list v-if="account.role === 1" textline="three-line">
          <mu-sub-header>Appointment</mu-sub-header>
          <div v-for="(appointment, index) in appointmentList" :key="index" @click="openSchedule(appointment)">
            <mu-list-item avatar button>
              <mu-list-item-action>
                <mu-avatar>
                  <img src="@/assets/image/demo/avatar.png">
                </mu-avatar>
              </mu-list-item-action>
              <mu-list-item-content>
                <mu-list-item-title>{{ appointment.patient.name }}</mu-list-item-title>
                <mu-list-item-sub-title>
                  <span style="color: rgba(0, 0, 0, .87)">{{ appointment.patient.patient.diagnosis }}</span>
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
    <mu-dialog :open.sync="openAppointment" title="Dialog">
      <mu-date-input v-model="appointment.date" :date-time-format="enDateFormat" icon="today" label="Date" container="dialog" disabled label-float full-width/>
      <mu-date-input v-model="appointment.time" icon="today" label="Time" container="dialog" type="time" disabled label-float full-width/>
      <mu-text-field v-model="appointment.content" :rows="4" disabled multi-line full-width/>
      <mu-button slot="actions" flat color="primary" @click="acceptAppointment">Accept</mu-button>
      <mu-button slot="actions" flat color="primary" @click="denyAppointment">Deny</mu-button>
    </mu-dialog>
  </div>
</template>

<script>
import Toast from 'muse-ui-toast'
import { mapGetters } from 'vuex'
import { getAppointmentByDoctorId, updateAppointmentStatus } from '@/api/appointment'

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
  name: 'Schedule',
  data() {
    return {
      appointmentList: [],
      openAppointment: false,
      appointment: {},
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
    const that = this
    getAppointmentByDoctorId(this.account.id).then((response) => {
      if (response.code === 200) {
        that.appointmentList = response.data
        this.loading = false
      }
    }).catch(() => {
      this.loading = false
    })
  },
  methods: {
    openSchedule(appointment) {
      this.appointment = appointment
      this.openAppointment = true
    },
    acceptAppointment() {
      updateAppointmentStatus(this.appointment.id, 1).then((response) => {
        if (response.code === 200) {
          this.appointment.status = 1
          Toast.success('Appointment accepted.')
          this.openAppointment = false
        }
      }).catch(() => {
        Toast.error('Failed accepting appointment.')
        this.openAppointment = false
      })
    },
    denyAppointment() {
      updateAppointmentStatus(this.appointment.id, 2).then((response) => {
        if (response.code === 200) {
          this.appointment.status = 2
          Toast.success('Appointment denied.')
          this.openAppointment = false
        }
      }).catch(() => {
        Toast.error('Failed denying appointment.')
        this.openAppointment = false
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .schedule {
    &-appointment {
      margin-top: 1.3rem;
      width: 100%;
      overflow: hidden;
      margin-bottom: 1.3rem;
    }
  }
</style>
