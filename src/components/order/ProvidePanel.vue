<template>
  <el-form
    :model="ruleForm"
    status-icon
    :rules="rules"
    ref="ruleForm"
    label-width="120px"
    class="demo-ruleForm"
    @keyup.enter="submitForm('fuleForm')"
  >
    <el-form-item label="MainOrder" prop="mainorder">
      <el-input v-model="ruleForm.mainorder" :disabled="true"></el-input>
    </el-form-item>
    <el-form-item label="Quantity" prop="quantity">
      <el-input v-model="ruleForm.quantity" auto-complete="off" @keyup.enter="submitForm('fuleForm')"></el-input>
    </el-form-item>
    <el-form-item label="Comments" prop="comments">
      <el-input v-model="ruleForm.comments" type="textarea" :rows="3"></el-input>
    </el-form-item>
    <el-form-item label="Phone" prop="phone">
      <el-input v-model="ruleForm.phone"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')" >Submit</el-button>
      <el-button @click="resetForm('ruleForm')">Reset</el-button>
    </el-form-item>
  </el-form>
</template>


<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import validator from 'validator';

interface Callback {
    (err?: Error): any
};

interface LoginComponent extends Vue{
  resetFields(): void,
  validate(valid: object): boolean
}

@Component
export default class Login extends Vue {
    @Prop() quantity!: number;
    userid: string = sessionStorage.getItem('userid') as string;
    ruleForm = {
      mainorder: '',
      comments: '',
      quantity: '',
      phone: '',
    }
    beforeMount() {
        this.ruleForm.mainorder = this.$route.params.orderid;
    }
    checkNothing(a: object, b: object, callback: Callback) { callback(); }
    checkNumber(rule: Object, value: string, callback: Callback) {
        if (!validator.isNumeric(value)) {
            callback(new Error('This field should be digits'));
            return;
        }
        callback();
    }
    checkPhone(rule: Object, value: string, callback: Callback) {
        if (value == '') {
            callback();
            return;
        }
        if (!validator.isMobilePhone(value, 'any')) {
            callback(new Error('Please enter a valid phone number'));
            return;
        }
        callback();
    }
    rules = {
        comments: [{ validator: this.checkNothing, trigger: "blur"}],
        quantity: [{ validator: this.checkNumber, trigger: "blur"}],
        phone: [{ validator: this.checkPhone, trigger: "blur"}]
    }
    submitForm(formName: string) {
      console.log(formName);
      (this.$refs[formName] as LoginComponent).validate((valid: any) => {
        if (valid) {
            console.log({...this.ruleForm, ...{userid: this.userid}});
            fetch(`/api/order/subOrder`, {
                method: 'POST',
                body: JSON.stringify({
                    ...this.ruleForm,
                    ...{ createuser: this.userid }
                })
            }).then(res => res.json())
            .then(res => {
                if (res.code === 0) {
                    alert('ok');
                } else {
                    alert(`err: res.msg`);
                }
            })
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