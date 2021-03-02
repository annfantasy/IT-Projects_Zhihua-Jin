<template>
  <div v-loading="loading" class="questionnaire">
    <mu-appbar style="width: 100%;" title="My Questionnaire" color="primary">
      <mu-button slot="left" icon @click="$router.push('/health/index')">
        <mu-icon value="arrow_back"/>
      </mu-button>
    </mu-appbar>
    <mu-expansion-panel :expand="panel === 'panel1'" @change="toggle('panel1')">
      <div slot="header">New questionnaire</div>
      <mu-container>
        <mu-list textline="three-line">
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I cough all the time</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[0]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[0]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">My chest is full of phlegm (mucus)</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[1]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[1]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">My chest feels very tight</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[2]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[2]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">When I walk up a hill or a flight of stairs I am completely out of breath</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[3]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[3]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I am completely limited to doing all activities at home</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[4]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[4]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I am not confident leaving my home at all because of my lung condition</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[5]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[5]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I do not sleep soundly because of my lung condition</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[6]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[6]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I have no energy at all</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[7]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[7]" :min="1" :max="5" :display-value="false"/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-button full-width color="primary" @click="submitQuestionnaire">Submit</mu-button>

        </mu-list>
      </mu-container>
    </mu-expansion-panel>

    <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
      <div slot="header">Questionnaire History</div>
      <mu-card v-for="(questionnaire, index) in questionnaireList" :key="index">
        <mu-list textline="three-line">
          <mu-sub-header>{{ questionnaire.createDate.split('T')[0] + ' ' + questionnaire.createDate.split('T')[1].split('.')[0] }}</mu-sub-header>
          <mu-sub-header>{{ 'Health Status: ' + questionnaire.result }}</mu-sub-header>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I cough all the time</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[0]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[0]" :min="1" :max="5" :display-value="false" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">My chest is full of phlegm (mucus)</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[1]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[1]" :min="1" :max="5" :display-value="false" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">My chest feels very tight</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[2]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[2]" :min="1" :max="5" :display-value="false" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">When I walk up a hill or a flight of stairs I am completely out of breath</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[3]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[3]" :min="1" :max="5" :display-value="false" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I am completely limited to doing all activities at home</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[4]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[4]" :min="1" :max="5" :display-value="false" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I am not confident leaving my home at all because of my lung condition</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[5]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[5]" :min="1" :max="5" :display-value="false" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I do not sleep soundly because of my lung condition</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[6]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[6]" :min="1" :max="5" :display-value="false" disabled/>
            </mu-list-item-content>
          </mu-list-item>
          <mu-divider/>
          <mu-list-item button class="questionnaire-item">
            <mu-list-item-content>
              <div class="questionnaire-item-title">I have no energy at all</div>
              <div class="questionnaire-item-text">{{ detailText(questionnaire.detailArray[7]) }}</div>
              <mu-slider :step="1" v-model="questionnaire.detailArray[7]" :min="1" :max="5" :display-value="false" disabled/>
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
import { getQuestionnaireList, postQuestionnaire } from '@/api/questionnaire'

export default {
  name: 'Questionnaire',
  data() {
    return {
      loading: true,
      panel: '',
      questionnaireList: [],
      questionnaire: {
        detail: '',
        detailArray: [1, 1, 1, 1, 1, 1, 1, 1],
        patientId: undefined
      }
    }
  },
  computed: {
    ...mapGetters([
      'account'
    ]),
    detailText() {
      return function(value) {
        let text = 'Unknown'
        switch (value) {
          case 1:
            text = 'Strongly disagree'
            break
          case 2:
            text = 'Disagree'
            break
          case 3:
            text = 'Neutral'
            break
          case 4:
            text = 'Agree'
            break
          case 5:
            text = 'Strongly agree'
            break
        }
        return text
      }
    }
  },
  mounted() {
    this.loading = false
    this.questionnaire.patientId = this.account.id
    this.getQuestionnaireList()
  },
  methods: {
    toggle(panel) {
      this.panel = panel === this.panel ? '' : panel
    },
    submitQuestionnaire() {
      this.questionnaire.detail = this.questionnaire.detailArray.toString()
      postQuestionnaire(this.questionnaire).then(response => {
        if (response.code === 200) {
          this.questionnaire = {
            detail: '',
            detailArray: [1, 1, 1, 1, 1, 1, 1, 1],
            patientId: this.account.id
          }
          this.getQuestionnaireList()
        }
        const result = response.data.result
        if (result === 'High' || result === 'Very High') {
          Toast.success('Result is ' + result + '. Please make an appointment.')
          this.$router.push('/health/index')
        } else {
          Toast.success('Result is ' + result)
        }
      }).catch(() => {
        this.loading = false
      })
    },
    getQuestionnaireList() {
      this.questionnaireList = []
      getQuestionnaireList(this.account.id).then((response) => {
        if (response.code === 200) {
          for (const questionnaire of response.data) {
            questionnaire.detailArray = []
            const detail = questionnaire.detail.split(',')
            detail.forEach(item => {
              questionnaire.detailArray.push(+item)
            })
            this.questionnaireList.push(questionnaire)
          }
        }
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.questionnaire {

    &-item {
      height: 6rem;
      &-title {
        margin-top: 1rem;
      }

      &-text {
        font-weight: bold;
      }
    }

}
</style>
