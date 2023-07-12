import request from "./use-axios";

export async function getCoverAll(body?: CoverData) {
  const { data } = await request.post("/select/all/cover", body || {});
  return data;
}

export async function getSmokeAll(body?: SmokeData) {
  const { data } = await request.post("/select/all/smoke", body || {});
  return data;
}

export async function getCoverCount() {
  const { data } = await request.post("/get/cover/count");
  return data;
}

export async function getSmokeCount() {
  const { data } = await request.post("/get/smoke/count");
  return data;
}

export async function getRecentCoverAndSmoke() {
  const { data } = await request.post("/get/recent/coverAndSmoke");
  return data;
}
