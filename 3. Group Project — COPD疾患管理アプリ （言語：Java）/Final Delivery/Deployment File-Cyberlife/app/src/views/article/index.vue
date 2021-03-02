<template>
  <div v-loading="loading" class="article">
    <mu-appbar color="lightBlue400" class="article-appbar">
      <mu-button slot="left" icon @click="$router.go(-1)">
        <mu-icon value="arrow_back"/>
      </mu-button>
      {{ article.title }}
      <mu-button slot="right" icon>
        <mu-icon value="share"/>
      </mu-button>
    </mu-appbar>
    <mu-container v-model="article" class="article-info">
      <mu-card-title :title="article.title" :sub-title="article.createDate"/>
      <mu-card class="article-info-user">
        <mu-ripple>
          <mu-card-header :title="article.author" sub-title="COPD system administrator">
            <mu-avatar slot="avatar">
              <img :src="defaultAvatar">
            </mu-avatar>
          </mu-card-header>
        </mu-ripple>
      </mu-card>
      <mu-card class="article-info-content">
        <mu-ripple>
          <mu-card-text>
            {{ article.content }}
          </mu-card-text>
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
</template>

<script>
import { mapGetters } from 'vuex'
import { getArticle } from '@/api/article'
import { replyList, avatar } from '@/utils/demoData'

export default {
  name: 'Article',
  data() {
    return {
      loading: true,
      defaultAvatar: avatar,
      article: {},
      replyList: replyList
    }
  },
  computed: {
    ...mapGetters([
      'account'
    ])
  },
  mounted() {
    this.loading = false
    const articleId = this.$router.currentRoute.params.id
    if (!articleId) {
      this.$router.replace('/error/404')
    }
    const that = this
    getArticle(articleId).then((response) => {
      if (response.code === 200) {
        that.article = response.data
        this.loading = false
      }
    }).catch(() => {
      this.loading = false
    })
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.article {

  &-appbar {
    position: fixed;
    width: 100%;
    top: 0;
    margin: auto;
    z-index: 999;
  }

  &-info{
    padding-top: 5rem;
    margin-bottom: 1.3rem;

    &-user {
      margin-bottom: 0.6rem;
    }

    &-content{
      margin-bottom: 1.3rem;
    }
  }

  &-reply {
    &-card {
      margin-bottom: 0.6rem;
    }
  }
}
</style>
