<template>
  <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="Comment">
            <span>{{ props.row.comments }}</span>
          </el-form-item>
          <el-form-item label="Create Date">
            <span>{{ props.row.createdate }}</span>
          </el-form-item>
          <el-form-item label="Create User">
            <span>{{ props.row.createuser }}</span>
          </el-form-item>
          <el-form-item label="Id">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="Main Order Id">
            <span>{{ props.row.mainOrderId }}</span>
          </el-form-item>
          <el-form-item label="Phone">
            <span>{{ props.row.phone }}</span>
          </el-form-item>
          <el-form-item label="Quantity">
            <span>{{ props.row.quantity }}</span>
          </el-form-item>
          <el-form-item label="Status">
            <span>{{ props.row.status }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      sortable
      label="ID"
      prop="id">
    </el-table-column>
    <el-table-column
      sortable
      label="Main Order Id"
      prop="mainorder">
    </el-table-column>
    <el-table-column
      sortable
      label="Create User ID"
      prop="createuser">
    </el-table-column>
    <el-table-column
      sortable
      label="Quantity"
      prop="quantity">
    </el-table-column>
    <el-table-column label="Operation" v-if="role == 'manager'">
      <template slot-scope="scope">
        <el-button type="danger" icon="el-icon-delete" circle v-if="role == 'manager'"
         @click="deleteOrder(scope.$index, scope.row)">
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
interface TableDataInterface {
  comments: string,
  createdate: string,
  createuser: number,
  id: string,
  mainorder: string,
  phone: string,
  quantity: number,
  status: number,
}
@Component
export default class Button extends Vue {
  @Prop() tableData !: TableDataInterface[];

  role: string = '';
  beforeMount() {
    this.role = sessionStorage.getItem('role') as string;
  }
  deleteOrder(index: number, row: TableDataInterface) {
    // TODO: to be finished
    fetch(`/api/order/subOrder/${row.id}/cancel`)
    .then(res => res.json())
    .then(res => {
      if (res.code === 0) {
        this.$message({
          message: `successfully cancel order ${row.id}`,
          type: "success"
        })
        this.tableData[index].status = 4;
      } else {
        this.$message({
          message: `failed: ${res.msg}`,
          type: "error"
        })
      }
    }).catch(err => {
      this.$message({
        message: `${err}`,
        type: "error"
      })
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