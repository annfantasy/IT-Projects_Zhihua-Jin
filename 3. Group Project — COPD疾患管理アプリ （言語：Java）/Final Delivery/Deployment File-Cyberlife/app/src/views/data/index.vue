<template>
  <div v-loading="loading" class="data">
    <mu-appbar style="width: 100%;" title="Data" color="primary"/>
    <mu-expansion-panel :expand="panel === 'panel1'" @change="toggle('panel1')">
      <div slot="header">New Health Record</div>
      <mu-container>
        <mu-list textline="three-line">
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How many times have you smoked?</div>
              <mu-text-field v-model="healthRecord.detailArray[0]"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How many times have you done exercise?</div>
              <mu-text-field v-model="healthRecord.detailArray[1]"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">Have your respiratory problem become worse?</div>
              <mu-text-field v-model="healthRecord.detailArray[2]"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">Have you received any treatment on your symptom?</div>
              <mu-text-field v-model="healthRecord.detailArray[3]"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How much air you can push out in 1 second? (This is also called FEV1, leave blank if you do not know the value)</div>
              <mu-text-field v-model="healthRecord.detailArray[4]"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-button full-width color="primary" @click="submitHealthRecord">Submit</mu-button>
        </mu-list>
      </mu-container>
    </mu-expansion-panel>

    <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
      <div slot="header">Health Record History</div>
      <mu-card v-for="(healthRecord, index) in healthRecordList" :key="index" class="questionnaire-container-post">
        <mu-list textline="three-line">
          <mu-sub-header>{{ healthRecord.createDate.split('T')[0] + ' ' + healthRecord.createDate.split('T')[1].split('.')[0] }}</mu-sub-header>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How many times have you smoked?</div>
              <mu-text-field v-model="healthRecord.detailArray[0]" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How many times have you smoked?</div>
              <mu-text-field v-model="healthRecord.detailArray[1]" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How many times have you smoked?</div>
              <mu-text-field v-model="healthRecord.detailArray[2]" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How many times have you smoked?</div>
              <mu-text-field v-model="healthRecord.detailArray[3]" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="data-item">
            <mu-list-item-content>
              <div class="data-item-title">How many times have you smoked?</div>
              <mu-text-field v-model="healthRecord.detailArray[4]" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
        </mu-list>
      </mu-card>
    </mu-expansion-panel>
  </div>
</template>

<script>
import Toast from 'muse-ui-toast'
import { mapGetters } from 'vuex'
import { getHealthRecordList, postHealthRecord } from '@/api/healthRecord'

export default {
  name: 'Data',
  data() {
    return {
      loading: true,
      panel: '',
      healthRecordList: [],
      healthRecord: {
        detail: '',
        detailArray: ['', '', '', '', ''],
        patientId: undefined
      }
    }
  },
  computed: {
    ...mapGetters([
      'account'
    ])
  },
  mounted() {
    this.loading = false
    this.healthRecord.patientId = this.account.id
    this.getHealthRecordList()
  },
  methods: {
    toggle(panel) {
      this.panel = panel === this.panel ? '' : panel
    },
    submitHealthRecord() {
      const that = this
      this.healthRecord.detail = this.healthRecord.detailArray.toString()
      postHealthRecord(this.healthRecord).then(response => {
        if (response.code === 200) {
          that.healthRecord = {
            detail: '',
            detailArray: ['', '', '', '', ''],
            patientId: that.account.id
          }
          that.getHealthRecordList()
        }
        Toast.success('Your health record has been saved.')
      }).catch(() => {
        this.loading = false
      })
    },
    getHealthRecordList() {
      this.healthRecordList = []
      getHealthRecordList(this.account.id).then((response) => {
        if (response.code === 200) {
          for (const healthRecord of response.data) {
            healthRecord.detailArray = []
            const detail = healthRecord.detail.split(',')
            detail.forEach(item => {
              healthRecord.detailArray.push(item)
            })
            this.healthRecordList.push(healthRecord)
          }
        }
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.data {
  &-item {
    height: 7rem;
    &-title {
      margin-top: 2rem;
    }

    &-text {
      font-weight: bold;
    }
  }
}
</style>
