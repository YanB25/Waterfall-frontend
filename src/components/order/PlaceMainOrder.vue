<template>
  <el-form
    :model="ruleForm"
    status-icon
    :rules="rules"
    ref="ruleForm"
    label-width="120px"
    class="demo-ruleForm"
  >
    <el-form-item label="Name" prop="name">
      <el-input v-model="ruleForm.name"></el-input>
    </el-form-item>
    <el-form-item label="Summary" prop="summary">
      <el-input v-model="ruleForm.summary" type="textarea" :rows="3"></el-input>
    </el-form-item>
    <el-form-item label="Address" prop="address">
      <el-input v-model="ruleForm.address"></el-input>
    </el-form-item>
    <el-form-item label="Comments" prop="comments">
      <el-input v-model="ruleForm.comments" type="textarea" :rows="3" placeholder="Optinal"></el-input>
    </el-form-item>
    <!-- create date -->
    <!-- create user -->
    <el-form-item label="Deadline" prop="_deadline">
        <div >
            <!-- <span class="demonstration">Deadline</span> -->
            <el-date-picker
            v-model="ruleForm._deadline"
            type="date"
            placeholder="Choose a date">
            </el-date-picker>
        </div>
    </el-form-item>
    <el-form-item label="Price" prop="price">
      <el-input v-model="ruleForm.price"></el-input>
    </el-form-item>
    <el-form-item label="Quantity" prop="quantity">
      <el-input v-model="ruleForm.quantity"></el-input>
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
export default class PlaceMainOrder extends Vue {
    ruleForm = {
        name: '',
        summary: '',
        address: '',
        comments: '',
        _deadline: new Date(), // what user input
        deadline: '', // a string to send
        price: '',
        quantity: '',
        createuser: '',
    }
    checkAscii(rule: object, value: string, callback: Callback) {
        if (!value || !validator.isAscii(value)) {
            callback(new Error("Should not be empty and ONLY letters and numbers and common punctuations are allowed."));
            return;
        }
        callback();
    }
    checkNothing(rule: object, value: string, callback: Callback) { callback();}
    checkDeadline(rule: object, value: Date, callback: Callback) {
        // console.log(this.ruleForm._deadline);
        console.log(value);
        console.log(this.buildTimeString(value));
        if (value < new Date()) {
            callback(new Error("Deadline should not be in the past."));
            return;
        }
        callback();
    }
    checkNumber(rule: object, value: string, callback: Callback) {
        if (!value || !validator.isNumeric(value)) {
            callback(new Error("Should not be empty and ONLY digits are allowed"));
            return;
        }
        callback();
    }
    buildTimeString(value: Date) {
        // return `${value.getFullYear()}-${value.getMonth()}-${value.getDate()} ${value.getHours()}:${value.getMinutes()}:${value.getSeconds()}`
        return `${value.getFullYear()}-${value.getMonth()}-${value.getDate()}`
        // return value.toISOString().replace(/T/, ' ').replace(/\..+/, '') 
    }
  rules = {
      name: [{ validate: this.checkNothing, trigger: "blur"}],
      summary: [{ validator: this.checkNothing, trigger: "blur"}],
      address: [{ validator: this.checkNothing, trigger: "blur" }],
      comments: [{ validator: this.checkNothing, trigger: "blur" }],
      _deadline: [{ validator: this.checkDeadline, trigger: "blur" }],
      price: [{ validator: this.checkNumber, trigger: "blur"}],
      quantity: [{ validator: this.checkNumber, trigger: "blur"}],
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
  ]
  submitForm(formName: string) {
    console.log(formName);
    (this.$refs[formName] as SignUpComponent).validate((valid: any) => {
      if (valid) {
        this.ruleForm['deadline'] = this.buildTimeString(this.ruleForm._deadline);
        // this.ruleForm['createuser'] = sessionStorage.getItem('userid') as string;
        fetch("/api/order/mainOrder", {
          method: "POST",
          body: JSON.stringify(this.ruleForm)
        })
          .then(res => {
            return res.json();
          })
          .then(res => {
              if (res.code === 0) {
                  this.$message({
                    message: 'success!',
                    type: 'success'
                  })
              } else {
                 this.$message({
                   message: `fail: ${res.data.msg}`,
                   type: "error"
                 });
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