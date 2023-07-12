<script setup lang="ts">
import * as echarts from "echarts";
import { getCoverCount, getSmokeCount, getRecentCoverAndSmoke } from "@/apis";

const coverCount = await getCoverCount();
const smokeCount = await getSmokeCount();
const recentCoverAndSmoke = await getRecentCoverAndSmoke();

const coverCountInst = ref();
const smokeCountInst = ref();
const coverAndSmokeInst = ref();

onMounted(async () => {
  const coverAndSmokeChart = echarts.init(coverAndSmokeInst.value);

  coverAndSmokeChart.setOption({
    tooltip: {
      trigger: "axis",
      axisPointer: { type: "cross" }
    },
    xAxis: [
      {
        type: "category",
        axisTick: {
          alignWithLabel: true
        },
        data: recentCoverAndSmoke.dates
      }
    ],
    yAxis: [
      {
        type: "value",
        name: "井盖",
        min: 0,
        max: 100,
        position: "right",
        axisLabel: {
          formatter: "{value} accel x"
        }
      },
      {
        type: "value",
        name: "烟雾",
        min: 0,
        max: 3000,
        position: "left",
        axisLabel: {
          formatter: "{value} db/m"
        }
      }
    ],
    series: [
      {
        name: "井盖",
        type: "bar",
        yAxisIndex: 0,
        data: recentCoverAndSmoke.covers
      },
      {
        name: "烟雾",
        type: "line",
        smooth: true,
        yAxisIndex: 1,
        data: recentCoverAndSmoke.smokes
      }
    ]
  });

  const coverCountChart = echarts.init(coverCountInst.value);

  coverCountChart.setOption({
    tooltip: {
      trigger: "item"
    },
    legend: {
      orient: "vertical",
      left: "left"
    },
    series: [
      {
        type: "pie",
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)"
          }
        },
        data: [
          {
            value: coverCount.normal,
            name: `正常(${coverCount.normal})`
          },
          {
            value: coverCount.warning,
            name: `异常(${coverCount.warning})`
          }
        ]
      }
    ]
  });

  const smokeCountChart = echarts.init(smokeCountInst.value);

  smokeCountChart.setOption({
    tooltip: {
      trigger: "item"
    },
    legend: {
      orient: "vertical",
      left: "left"
    },
    series: [
      {
        type: "pie",
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)"
          }
        },
        data: [
          {
            value: smokeCount.normal,
            name: `正常(${smokeCount.normal})`
          },
          {
            value: smokeCount.warning,
            name: `异常(${smokeCount.warning})`
          }
        ]
      }
    ]
  });
});
</script>

<template>
  <div>
    <div class="font-bold text-1.2rem mb-10 mt-5">最近10次井盖X轴和烟雾值数据</div>
    <div class="w-100% h-400px" ref="coverAndSmokeInst"></div>
  </div>
  <div>
    <div class="font-bold text-1.2rem mb-10 mt-5">井盖报警次数</div>
    <div class="w-100% h-400px" ref="coverCountInst"></div>
  </div>
  <div>
    <div class="font-bold text-1.2rem mb-10 mt-5">烟雾报警次数</div>
    <div class="w-100% h-400px" ref="smokeCountInst"></div>
  </div>
</template>

<style scoped lang="scss"></style>
