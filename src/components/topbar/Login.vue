<template>
  <el-form
    :model="ruleForm"
    status-icon
    :rules="rules"
    ref="ruleForm"
    label-width="120px"
    class="demo-ruleForm"
  >
    <el-form-item label="User Name" prop="username">
      <el-input v-model.number="ruleForm.username"></el-input>
    </el-form-item>
    <el-form-item label="Password" prop="pass">
      <el-input type="password" v-model="ruleForm.pass" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">Submit</el-button>
      <el-button @click="resetForm('ruleForm')">Reset</el-button>
    </el-form-item>
  </el-form>
</template>


<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

interface Callback {
    (err?: Error): any
};

interface LoginComponent extends Vue{
  resetFields(): void,
  validate(valid: object): boolean
}

@Component
export default class Login extends Vue {
    checkUsername(rule: object, value :number, callback: Callback) {
      if (!value) {
        return callback(new Error("Please input user name"));
      }
      setTimeout(() => {
        callback();
      }, 1000);
    }
    validatePass(rule: object, value: string, callback: Callback) {
      if (value === "") {
        callback(new Error("Please input the password"));
      } 
      else if (value.length < 6) {
        callback(new Error("Place enter password longer than 6 characters"))
      }
      callback();
    };
    ruleForm = {
      pass: "",
      username: "",
    }
    rules = {
      pass: [{ validator: this.validatePass, trigger: "blur" }],
      username: [{ validator: this.checkUsername, trigger: "blur" }]
    }
    submitForm(formName: string) {
      console.log(formName);
      (this.$refs[formName] as LoginComponent).validate((valid: any) => {
        if (valid) {
          fetch('/api/login', {
            method: 'POST',
            body: JSON.stringify({
              username: this.ruleForm.username,
              password: this.ruleForm.pass
            })
          })
          .then(res => {
            return res.json();
          })
          .then(data => {
            if (data.code === 0) {
              this.$emit('login', data.data.username);
            }
          })
          .catch(err => {
            console.log(err);
            
          })
          return true;
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    }
    resetForm(formName: string) {
      (this.$refs[formName] as LoginComponent).resetFields();
    }
};
</script>