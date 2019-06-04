<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    class="main">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="User ID">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="User Name">
            <span>{{ props.row.username }}</span>
          </el-form-item>
          <el-form-item label="Balance">
            <span>{{ props.row.balance }}</span>
          </el-form-item>
          <el-form-item label="Phone">
            <span>{{ props.row.phone }}</span>
          </el-form-item>
          <el-form-item label="E-mail">
            <span>{{ props.row.email }}</span>
          </el-form-item>
          <el-form-item label="User Type">
            <span>{{ props.row.role }}</span>
          </el-form-item>
          <el-form-item label="User Status">
            <span>{{ props.row.status }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      sortable
      label="User ID"
      prop="id">
    </el-table-column>
    <el-table-column
      sortable
      label="User Name"
      prop="username">
    </el-table-column>
    <el-table-column
      sortable
      label="Balance"
      prop="balance">
    </el-table-column>
    <el-table-column
      sortable
      label="User Type"
      prop="role">
    </el-table-column>
    <el-table-column
      sortable
      label="User Status"
      prop="status"
      :width="200">
      <template slot-scope="scope">
        <el-switch
        :value="!scope.row.status"
        active-text="Active"
        inactive-text="Inactive"
        @change="changeUserStatus(scope.$index, scope.row)">
        </el-switch>
      </template>
    </el-table-column>
    <el-table-column label="Operation" :width="200">
      <template slot-scope="scope">
          <!-- <el-tooltip content="查看详情" placement="bottom" :enterable=false>
          <el-button icon="el-icon-search" circle
          @click="info(scope.$index, scope.row)"></el-button>
        </el-tooltip> -->
          <el-tooltip content="Edit User Info" placement="bottom" :enterable=false>
          <el-button type="primary" icon="el-icon-edit" circle
          @click="info(scope.$index, scope.row)">
          </el-button>
        </el-tooltip>
        <el-tooltip content="Delete User" placement="bottom" :enterable=false>
          <el-button type="danger" icon="el-icon-delete" circle
          @click="deleteUser(scope.$index, scope.row)">
          </el-button>
        </el-tooltip>
      </template>
    </el-table-column>
  </el-table>
</template>
<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Table } from 'element-ui';
interface TableDataInterface {
  id : number,
  username : string,
  email : string,
  phone : string,
  balance : number,
  role : string,
  status : number,
}
@Component
export default class Button extends Vue {
  @Prop() tableData !: TableDataInterface[];
  changeUserStatus(index: number, row: TableDataInterface) {
    fetch(`/api/user/${row.id}`, {
      method: 'POST',
      body: JSON.stringify({
        status: 1 - row.status,
      })
    }).then(res => res.json())
    .then(res => {
      if (res.code === 0) {
        this.$message({
          message: `Successfully edited ${row.username}`,
          type: "success"
        })
        this.tableData[index].status = 1 - row.status;
      } else {
        this.$message({
          message: `err: ${res.msg}`,
          type: "error"
        })
      }
    }).catch(err => {
      this.$message({
        message: `err: ${err}`,
        type: "error"
      })
    })
  }
  deleteUser(index: number, row: object) {
    //TODO:
    this.$message({
      message: "not implemented",
      type: "error"
    })
  }
  info(index: number, row: TableDataInterface) {
    this.$router.push(`/profile/${row.id}`)
  }
  
}
</script>

<style>
  .main {
    margin-bottom: 100px;
  }
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