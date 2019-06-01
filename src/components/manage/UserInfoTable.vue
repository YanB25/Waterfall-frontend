<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    class="main">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="用户ID">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="用户名">
            <span>{{ props.row.username }}</span>
          </el-form-item>
          <el-form-item label="余额">
            <span>{{ props.row.balance }}</span>
          </el-form-item>
          <el-form-item label="电话">
            <span>{{ props.row.phone }}</span>
          </el-form-item>
          <el-form-item label="E-mail">
            <span>{{ props.row.email }}</span>
          </el-form-item>
          <el-form-item label="类型">
            <span>{{ props.row.role }}</span>
          </el-form-item>
          <el-form-item label="状态">
            <span>{{ props.row.status }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      sortable
      label="用户ID"
      prop="id">
    </el-table-column>
    <el-table-column
      sortable
      label="用户名"
      prop="username">
    </el-table-column>
    <el-table-column
      sortable
      label="用户余额"
      prop="balance">
    </el-table-column>
    <el-table-column
      sortable
      label="用户类型"
      prop="role">
    </el-table-column>
    <el-table-column
      sortable
      label="用户状态"
      prop="status">
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button icon="el-icon-search" circle
        @click="info(scope.$index, scope.row)"></el-button>
        <el-button type="primary" icon="el-icon-edit" circle
         @click="provide(scope.$index, scope.row)">
        </el-button>
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