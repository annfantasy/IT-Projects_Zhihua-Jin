<template>
  <div v-loading="loading" class="login">
    <mu-container>

      <mu-flex class="title" justify-content="center">
        <h1>COPD System</h1>
      </mu-flex>
      <mu-flex class="login-input-box" justify-content="center">
        <mu-form ref="loginForm" :model="loginForm" class="login-form">
          <mu-form-item :rules="loginRules.username" label="Username" label-float icon="account_circle" prop="username">
            <mu-text-field v-model="loginForm.username"/>
          </mu-form-item>
          <mu-form-item :rules="loginRules.password" label="Password" label-float icon="locked" prop="password">
            <mu-text-field
              v-model="loginForm.password"
              :action-icon="visibility ? 'visibility_off' : 'visibility'"
              :action-click="() => (visibility = !visibility)"
              :type="visibility ? 'text' : 'password'"/>
          </mu-form-item>
        </mu-form>
      </mu-flex>
      <mu-flex class="login-button-wrapper" justify-content="center">
        <mu-button round large full-width color="primary" @click="handleLogin">Sign in</mu-button>
      </mu-flex>
      <mu-flex class="login-button-wrapper" justify-content="center">
        <mu-button round large full-width color="secondary" @click="openRegisterDialog=true" >Sign up</mu-button>
      </mu-flex>
      <mu-flex class="login-button-wrapper" justify-content="center">
        <mu-button round large full-width color="success" @click="$router.push('/post')" >Admin Toolbox</mu-button>
      </mu-flex>
    </mu-container>
    <mu-container>
      <mu-dialog :open.sync="openRegisterDialog" transition="slide-bottom" fullscreen scrollable>
        <mu-appbar color="primary" title="Sign up">
          <mu-button slot="left" icon @click="openRegisterDialog=false">
            <mu-icon value="close"/>
          </mu-button>
          <mu-button slot="right" flat @click="handleRegistration">
            Done
          </mu-button>
        </mu-appbar>
        <mu-container>
          <mu-form ref="registerForm" :model="registerForm" class="login-register">
            <mu-form-item :rules="registerRules.username" label="Username" prop="username">
              <mu-text-field v-model="registerForm.username" prop="username"/>
            </mu-form-item>
            <mu-form-item :rules="registerRules.password" label="Password" prop="password">
              <mu-text-field v-model="registerForm.password" type="password" prop="password"/>
            </mu-form-item>
            <mu-form-item label="Name" prop="name">
              <mu-text-field v-model="registerForm.name" prop="name"/>
            </mu-form-item>
            <mu-select v-model="registerForm.gender" label="Gender" full-width>
              <mu-option v-for="(option,index) in gender" :key="index" :label="option" :value="index"/>
            </mu-select>
            <mu-select v-model="registerForm.role" label="Role" full-width>
              <mu-option v-for="(option,index) in role" :key="index" :label="option" :value="index"/>
            </mu-select>
            <mu-form-item label="Phone" prop="phone">
              <mu-text-field v-model="registerForm.phone" prop="phone"/>
            </mu-form-item>
            <mu-form-item label="Address" prop="address">
              <mu-text-field v-model="registerForm.address" prop="address"/>
            </mu-form-item>
          </mu-form>
        </mu-container>
      </mu-dialog>
      <mu-container/>
    </mu-container>
  </div>

</template>

<script>
import Toast from 'muse-ui-toast'
import { loginRules, registerRules } from '@/utils/validate'
import { register } from '@/api/login'

export default {
  name: 'Login',
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      registerForm: {
        username: '',
        password: '',
        name: '',
        gender: '',
        birthday: '',
        phone: '',
        address: '',
        role: ''
      },
      gender: [
        'Female', 'Male', 'Other'
      ],
      role: [
        'Patient', 'Doctor'
      ],
      loginRules: loginRules,
      registerRules: registerRules,
      visibility: false,
      openRegisterDialog: false,
      loading: false,
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    handleLogin() {
      this.$refs.loginForm.validate().then((result) => {
        if (result) {
          this.loading = true
          this.$store.dispatch('Login', this.loginForm).then(() => {
            this.loading = false
            this.$router.push({ path: this.redirect || '/' })
          }).catch(() => {
            this.loading = false
          })
        } else {
          return false
        }
      })
    },
    handleRegistration() {
      this.$refs.registerForm.validate().then((result) => {
        if (result) {
          this.loading = true
          register(this.registerForm).then((response) => {
            if (response.code === 200) {
              Toast.success('Sign up successfully.')
              this.loading = false
            }
          }).catch(() => {
            this.loading = false
          })
        } else {
          return false
        }
      })
      this.openRegisterDialog = false
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  $bg: #ffd5c2;
  .login {
    position: fixed;
    height: 100%;
    width: 100%;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    -moz-background-size: 100% 100%;
    background-color: $bg;

    .title {
      width: 100%;
      height: 100%;
      margin-top: 3rem;
    }

    .input-box {
      width: 100%;
      height: 100%;
      margin-top: 3rem;
      text-align: center;
    }

    &-button-wrapper {
      margin-bottom: 1.3rem;
    }

    &-register {
      padding: 1.3rem;
    }
  }

</style>
