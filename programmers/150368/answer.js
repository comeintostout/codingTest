function getNextStep(rateList) {
  let len = rateList.length;

  for (let i = len - 1; i >= 0; i--) {
    rateList[i] += 10;
    if (rateList[i] < 50) {
      break;
    } else {
      rateList[i] = 10;
    }
  }

  return rateList;
}

function calc(users, emoticons, rateList) {
  let answer = [0, 0];
  users.forEach((user, useri) => {
    const [userRate, userLimit] = user;

    let pay = 0;
    rateList.forEach((rate, idx) => {
      if (rate >= userRate) {
        pay += (emoticons[idx] * (100 - rate)) / 100;
      }
    });

    if (pay >= userLimit) {
      answer[0] += 1;
    } else {
      answer[1] += pay;
    }
  });

  return answer;
}

function solution(users, emoticons) {
  let answer = [0, 0];

  let rateList = [];
  emoticons.forEach((element) => {
    rateList.push(10);
  });
  let times = Math.pow(4, emoticons.length);
  let localAnswer = [];
  for (let i = 0; i <= times; i++) {
    localAnswer = calc(users, emoticons, rateList);

    if (localAnswer[0] > answer[0]) {
      answer = localAnswer;
    } else if (localAnswer[0] == answer[0] && localAnswer[1] > answer[1]) {
      answer = localAnswer;
    }

    rateList = getNextStep(rateList);
  }

  return answer;
}

console.log(
  solution(
    [
      [40, 2900],
      [23, 10000],
      [11, 5200],
      [5, 5900],
      [40, 3100],
      [27, 9200],
      [32, 6900],
    ],
    [1300, 1500, 1600, 4900]
  )
);
