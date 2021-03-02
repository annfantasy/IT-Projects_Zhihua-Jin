<template>
  <div v-loading="loading" class="post">
    <mu-button slot="left" icon @click="$router.push('/home')">
      <mu-icon value="arrow_back"/>
    </mu-button>
    <mu-form ref="postForm" :model="postForm" class="post-form">
      <mu-form-item :rules="postRules.title" label="Title" label-float prop="title" class="post-form-title">
        <mu-text-field v-model="postForm.title"/>
      </mu-form-item>
      <mu-form-item :rules="postRules.content" label="Content" label-float prop="content" class="post-form-content">
        <mu-text-field :rows="5" :rows-max="8" v-model="postForm.content" multi-line/>
      </mu-form-item>
      <mu-select v-model="postForm.tag" label="Tag" full-width>
        <mu-option v-for="(option,index) in tag" :key="index" :label="option" :value="index"/>
      </mu-select>
      <mu-form-item :rules="postRules.adminPassword" label="Admin Password" label-float prop="adminPassword" class="post-form-adminPassword">
        <mu-text-field v-model="postForm.adminPassword"/>
      </mu-form-item>
      <mu-button color="primary" @click="postArticle">Post</mu-button>
    </mu-form>
  </div>
</template>

<script>
import Toast from 'muse-ui-toast'
import { postArticle } from '@/api/article'
import { postRules } from '@/utils/validate'

export default {
  name: 'Post',
  data() {
    return {
      postForm: {
        title: '',
        content: '',
        createDate: '',
        adminPassword: 'admin'
      },
      tag: [
        'Trending',
        'Popular',
        'Focus'
      ],
      postRules: postRules,
      loading: true
    }
  },
  mounted() {
    this.loading = false
  },
  methods: {
    postArticle() {
      this.$refs.postForm.validate().then((result) => {
        if (result) {
          this.loading = true
          const date = new Date()
          this.postForm.createDate = date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate()
          postArticle(this.postForm).then((response) => {
            if (response.code === 200) {
              this.postForm = {
                title: '',
                content: '',
                adminPassword: 'admin'
              }
              Toast.success('Create article successfully.')
            }
            this.loading = false
          }).catch(() => {
            this.loading = false
          })
        } else {
          return false
        }
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.post {
  &-form {
    text-align: center;
    margin-top: 1rem;
    padding: 0 1.3rem 0 1.3rem;

    &-title {
      margin-bottom: 1.3rem;
    }

    &-content {
      margin-bottom: 1.3rem;
    }
  }
}
</style>
