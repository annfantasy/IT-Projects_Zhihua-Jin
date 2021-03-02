<template>
  <div v-loading="loading" class="home">
    <mu-carousel class="home-carousel" hide-indicators>
      <mu-carousel-item>
        <img :src="carouselImg[0]" @click="carouselClick(0)">
      </mu-carousel-item>
      <mu-carousel-item>
        <img :src="carouselImg[1]" @click="carouselClick(1)">
      </mu-carousel-item>
      <mu-carousel-item>
        <img :src="carouselImg[2]" @click="carouselClick(2)">
      </mu-carousel-item>
      <mu-carousel-item>
        <img :src="carouselImg[3]" @click="carouselClick(3)">
      </mu-carousel-item>
    </mu-carousel>
    <mu-container class="home-tab">
      <mu-tabs :value.sync="homeTabActive" color="green" indicator-color="yellow" full-width>
        <mu-tab>News</mu-tab>
        <mu-tab>Exercise</mu-tab>
        <mu-tab>Q&A</mu-tab>
      </mu-tabs>
      <div v-if="homeTabActive === 0" class="home-tab-content">
        <mu-container>
          <mu-card v-for="(article, index) in articleList[0]" :key="index" class="home-post-card">
            <mu-ripple @click="toArticleDetail(article)">
              <div class="home-post-card-title">{{ article.title }}</div>
              <mu-card-header :title="article.author" sub-title="COPD system administrator">
                <mu-avatar slot="avatar">
                  <img :src="defaultAvatar">
                </mu-avatar>
              </mu-card-header>
              <div class="home-post-card-text">
                {{ article.content }}
              </div>
            </mu-ripple>
            <mu-card-actions>
              <mu-flex align-items="center">
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="reply"/>
                  </mu-button>
                </mu-flex>
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="favorite" color="orange"/>
                  </mu-button>
                </mu-flex>
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="thumb_up" color="red"/>
                  </mu-button>
                </mu-flex>
              </mu-flex>
            </mu-card-actions>
          </mu-card>
        </mu-container>
      </div>
      <div v-if="homeTabActive === 1" class="home-tab-content">
        <mu-container>
          <mu-card v-for="(article, index) in articleList[1]" :key="index" class="home-post-card">
            <mu-ripple @click="toArticleDetail(article)">
              <div class="home-post-card-title">{{ article.title }}</div>
              <mu-card-header :title="article.author" sub-title="COPD system administrator">
                <mu-avatar slot="avatar">
                  <img :src="defaultAvatar">
                </mu-avatar>
              </mu-card-header>
              <div class="home-post-card-text">
                {{ article.content }}
              </div>
            </mu-ripple>
            <mu-card-actions>
              <mu-flex align-items="center">
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="reply"/>
                  </mu-button>
                </mu-flex>
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="favorite" color="orange"/>
                  </mu-button>
                </mu-flex>
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="thumb_up" color="red"/>
                  </mu-button>
                </mu-flex>
              </mu-flex>
            </mu-card-actions>
          </mu-card>
        </mu-container>
      </div>
      <div v-if="homeTabActive === 2" class="home-tab-content">
        <mu-container>
          <mu-card v-for="(article, index) in articleList[2]" :key="index" class="home-post-card">
            <mu-ripple @click="toArticleDetail(article)">
              <div class="home-post-card-title">{{ article.title }}</div>
              <mu-card-header :title="article.author" sub-title="COPD system administrator">
                <mu-avatar slot="avatar">
                  <img :src="defaultAvatar">
                </mu-avatar>
              </mu-card-header>
              <div class="home-post-card-text">
                {{ article.content }}
              </div>
            </mu-ripple>
            <mu-card-actions>
              <mu-flex align-items="center">
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="reply"/>
                  </mu-button>
                </mu-flex>
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="favorite" color="orange"/>
                  </mu-button>
                </mu-flex>
                <mu-flex justify-content="center" fill>
                  <mu-button>
                    <mu-icon left value="thumb_up" color="red"/>
                  </mu-button>
                </mu-flex>
              </mu-flex>
            </mu-card-actions>
          </mu-card>
        </mu-container>
      </div>
    </mu-container>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getArticleList } from '@/api/article'
import { carouselImg, avatar } from '@/utils/demoData'

export default {
  name: 'Home',
  data() {
    return {
      loading: true,
      carouselImg: carouselImg,
      defaultAvatar: avatar,
      articleList: [[], [], []],
      homeTabActive: 0
    }
  },
  computed: {
    ...mapGetters([
      'account'
    ])
  },
  mounted() {
    const that = this
    getArticleList().then((response) => {
      if (response.code === 200) {
        for (const post of response.data) {
          that.articleList[post.tag].push(post)
        }
        this.loading = false
      }
    }).catch(() => {
      this.loading = false
    })
  },
  methods: {
    toArticleDetail(article) {
      this.$router.push('article/' + article.id)
    },
    carouselClick(index) {
      switch (index) {
        case 0:
          this.$router.push('/health/index')
          break
        case 1:
          this.homeTabActive = 1
          break
        case 2:
          this.$router.push('/questionnaire')
          break
        case 3:
          this.homeTabActive = 2
          break
      }
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .home {
    &-appbar{
      position: fixed;
      width: 100%;
      top: 0;
      margin: auto;
      z-index: 999;
    }

    &-card-wrapper {
      text-align: center;
      margin: 5rem 0 1.3rem 0;

      .home-card {
        height: 6rem;
        margin: 0.5rem;

        img {
          width: 100%;
          height: 100%;
        }
      }
    }

    &-carousel {
      height: 10rem;
      margin-bottom: 1.3rem;
    }

    &-tab{
      margin-bottom: 1.3rem;
      &-content {
        height: 100%
      }
    }

    &-post-card{
      padding-top: 1rem;
      margin-bottom: 1.3rem;
      &-title {
        margin: auto 1.3rem 0.1rem 1.3rem;
        font-size: 1rem;
        font-weight: bold;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }

      &-text{
        margin: auto 1.3rem auto 1.3rem;
        height: 6.5rem;
        display: -webkit-box;
        -webkit-line-clamp: 5;
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }

    &-create-post-form {
      margin: 1.3rem 2rem 1.3rem 2rem;
    }
  }
</style>
