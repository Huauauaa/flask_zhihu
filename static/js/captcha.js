let button, timer, toast;

const onCaptchaClick = async () => {
  const email = document.querySelector('input[name="email"]').value;
  if (!email) {
    showAlert('请输入邮箱');
    return;
  }
  const payload = { email };
  const response = await fetch('/user/captcha', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  showAlert(data.message);
  if (data.code === 200) {
    button.removeEventListener('click', onCaptchaClick);

    let count = 60;
    timer = setInterval(() => {
      count -= 1;
      if (count > 0) {
        button.innerText = `${count}秒后重新发送`;
      } else {
        button.innerText = `获取验证码`;
        button.addEventListener('click', onCaptchaClick);
        clearInterval(timer);
      }
    }, 1e3);
  }
};

(() => {
  button = document.querySelector('button[data-name="captcha"]');

  button.addEventListener('click', onCaptchaClick);
})();
