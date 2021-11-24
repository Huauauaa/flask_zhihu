const showAlert = (message) => {
  const toastContainer = document.getElementById('alertToast');
  toastContainer.querySelector('.toast-body').innerText = message;
  toast = new bootstrap.Toast(toastContainer);
  toast.show();
};
