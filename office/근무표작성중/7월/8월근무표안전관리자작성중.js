let a = {'주간': '박병훈', '야간': '권헌일', '휴무1': '이영재', '휴무2': '엑스맨'};
let b = {'주간': '이영재', '야간': '박병훈', '휴무1': '권헌일', '휴무2': '엑스맨'};
let c = {'주간': '권헌일', '야간': '이영재', '휴무1': '박병훈', '휴무2': '엑스맨'};
let d = {'주간': '소장님', '야간': '이영재', '휴무1': '박병훈', '휴무2': '권헌일'};
let e = {'주간': '소장님', '야간': '박병훈', '휴무1': '권헌일', '휴무2': '이영재'};
let f = {'주간': '소장님', '야간': '권헌일', '휴무1': '이영재', '휴무2': '박병훈'};
let g = {'주간': '박병훈', '야간': '이영재', '휴무1': '권헌일', '휴무2': '엑스맨'};
let h = {'주간': '권헌일', '야간': '박병훈', '휴무1': '이영재', '휴무2': '엑스맨'};
let i = {'주간': '이영재', '야간': '권헌일', '휴무1': '박병훈', '휴무2': '엑스맨'};

let data = [a, b, c, d, e, f, g, h, i];

// Helper function to find the index of an object in the array
function findIndex(arr, obj) {
  return arr.findIndex((item) => JSON.stringify(item) === JSON.stringify(obj));
}

for (let _ = 0; _ < 1; _++) {
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, i)]);
}

for (let _ = 0; _ < 1; _++) {
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, g)]);
}

for (let _ = 0; _ < 1; _++) {
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, e)]);
  console.log(data[findIndex(data, d)]);
  console.log(data[findIndex(data, e)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, i)]);
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, g)]);
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, h)]);
  console.log(data[findIndex(data, h)]);
}
