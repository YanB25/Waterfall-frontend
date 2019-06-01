<template>
 <UserInfoTable :tableData="tableData">
 </UserInfoTable> 
</template>
<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import UserInfoTable from './UserInfoTable.vue'
interface TableDataInterface {
  id : number,
  username : string,
  email : string,
  phone : string,
  balance : number,
  role : string,
  status : number,
}
@Component({
  components: {
    UserInfoTable
  }
})
export default class Button extends Vue {
  tableData = []
  beforeCreate() {
    fetch('/api/user/users', {
      method: 'GET'
    }).then(data => {
      return data.json();
    }).then(res => {
      this.tableData = res.data.users;
    })
  }
}
</script>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>