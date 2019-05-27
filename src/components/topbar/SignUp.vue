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
    <el-form-item label="Confirm" prop="checkPass">
      <el-input type="password" v-model="ruleForm.checkPass" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item label="Email" prop="email">
      <el-input v-model.number="ruleForm.email"></el-input>
    </el-form-item>
    <el-form-item label="Phone" prop="phone">
      <el-input v-model="ruleForm.phone"></el-input>
    </el-form-item>

    <el-form-item label="User Type">
      <el-select v-model="ruleForm.usertype" placeholder="not chose yet">
        <el-option
          v-for="item in usertypes"
          :key="item.key"
          :label="item.label"
          :value="item.value"
        ></el-option>
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">Submit</el-button>
      <el-button @click="resetForm('ruleForm')">Reset</el-button>
    </el-form-item>
  </el-form>
</template>


<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import validator from 'validator';

interface Callback {
  (err?: Error): any;
}

interface SignUpComponent extends Vue {
  resetFields(): void;
  validate(valid: object): boolean;
}

@Component
export default class SignUp extends Vue {
  checkUsername(rule: object, value: number, callback: Callback) {
    if (!value) {
      return callback(new Error("Please input user name"));
    }
    const username = this.ruleForm.username;
    if (!validator.isAlphanumeric(username)){
      return callback(new Error("Username can only cantain a-z A-Z 0-9."));
    }
    setTimeout(() => {
      // let username = this.ruleForm.username;
      fetch(`/api/user/checkuser/${username}`)
        .then(res => {
          return res.json();
        })
        .then(data => {
          if (data.code === 0) {
            callback();
          } else {
            callback(new Error(data.data.msg));
          }
        });
      // callback();
    }, 1000);
  }
  checkPhone(rule: object, value: number, callback: Callback) {
    if (!validator.isMobilePhone(this.ruleForm.phone, 'any')) {
      return callback(new Error("please enter valid phone"));
    }
    callback();
  }
  checkEmail(rule: object, value: number, callback: Callback) {
    if (!validator.isEmail(this.ruleForm.email)) {
      return callback(new Error("Please enter valid email"));
    }
    callback();
  }

  validatePass(rule: object, value: string, callback: Callback) {
    if (value === "") {
      callback(new Error("Please input the password"));
    } else if (value.length < 6) {
      callback(new Error("Place enter password longer than 6 characters"));
    } else {
      if (this.ruleForm.checkPass !== "") {
        (this.$refs.ruleForm as any).validateField("checkPass");
      }
      callback();
    }
  }
  validatePass2(rule: object, value: string, callback: Callback) {
    if (value === "") {
      callback(new Error("Please input the password again"));
    } else if (value !== this.ruleForm.pass) {
      callback(new Error("Two inputs don't match!"));
    } else {
      callback();
    }
  }
  ruleForm = {
    pass: "",
    checkPass: "",
    username: "",
    usertype: "",
    phone: "",
    email: "",
  };
  rules = {
    pass: [{ validator: this.validatePass, trigger: "blur" }],
    checkPass: [{ validator: this.validatePass2, trigger: "blur" }],
    username: [{ validator: this.checkUsername, trigger: "blur" }],
    phone: [{ validator: this.checkPhone, trigger: "blur" }],
    email: [{ validator: this.checkEmail, trigger: "blur"}],
  };
  usertypes = [
    {
      key: 0,
      value: "provider",
      label: "provider"
    },
    {
      key: 1,
      value: "customer",
      label: "customer"
    },
    // {
    //   key: 2,
    //   value: "manager",
    //   label: "manager"
    // }
  ]
  submitForm(formName: string) {
    console.log(formName);
    (this.$refs[formName] as SignUpComponent).validate((valid: any) => {
      if (valid) {
        fetch("/api/user/register", {
          method: "POST",
          body: JSON.stringify({
            username: this.ruleForm.username,
            password: this.ruleForm.pass,
            email: this.ruleForm.email,
            phone: this.ruleForm.phone,
            role: this.ruleForm.usertype
          })
        })
          .then(res => {
            return res.json();
          })
          .then(data => {
            if (data.code === 0) {
              this.$emit("login", this.ruleForm.username, data.data.userid, this.ruleForm.usertype);
            }
          })
          .catch(err => {
            console.log(err);
          });
        return true;
      } else {
        console.log("error submit!!");
        return false;
      }
    });
  }
  resetForm(formName: string) {
    (this.$refs[formName] as SignUpComponent).resetFields();
  }
}
</script>