<script setup lang="ts">
import { getCoverAll } from "@/apis";

const coverList = shallowRef();
const nowPageNum = ref(1);
const nowPageSize = ref(15);

async function fetchData() {
  coverList.value = await getCoverAll({
    pageNum: nowPageNum.value,
    pageSize: nowPageSize.value
  });
}

watch(nowPageNum, async () => {
  await fetchData();
});

watch(nowPageSize, async () => {
  await fetchData();
});

await fetchData();
</script>

<template>
  <!-- <div class="mt-5 mb-5">
    <el-form ref="formInst" label-width="100px" label-position="left" :model="formData">
      <el-form-item label="日期" prop="date">
        <el-date-picker
          v-model="formData.date"
          value-format="YYYY-MM-DD"
          type="date"
          placeholder="选择一个日期时间" />
      </el-form-item>
      <el-form-item label="LED2 状态" prop="ledState">
        <el-select v-model="formData.ledState">
          <el-option v-for="item in ledState" :value="item.value" :label="item.label"> </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="传感器状态" prop="state">
        <el-select v-model="formData.state">
          <el-option v-for="item in state" :value="item.value" :label="item.label"> </el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <div class="f-c-c mt-5">
      <el-button @click="selectBy" type="primary" plain>条件查询</el-button>
    </div>
  </div>
    -->
  <div class="f-c-e">
    <el-pagination
      class="mb-5"
      background
      layout="sizes, prev, pager, next"
      :page-sizes="[10, 15, 20, 25, 30, 40, 50, 60]"
      :total="coverList.total"
      v-model:page-size="nowPageSize"
      v-model:current-page="nowPageNum" />
  </div>

  <el-table border :data="coverList.list" style="width: 100%">
    <el-table-column sortable prop="id" label="ID" width="150" show-overflow-tooltip />
    <el-table-column sortable prop="date" label="日期" show-overflow-tooltip />
    <el-table-column sortable prop="accelX" label="Accel X" />
    <el-table-column sortable prop="accelY" label="Accel Y" />
    <el-table-column sortable prop="accelZ" label="Accel Z" />
    <el-table-column sortable prop="temp" label="温度" />
    <el-table-column sortable prop="coverStatus" label="状态" width="150" />
    <el-table-column prop="name" label="姓名" />
    <el-table-column prop="sno" label="学号" />
  </el-table>
</template>

<style scoped lang="scss"></style>
