const formEle = document.querySelector('form');

formEle.addEventListener('submit', async (e) => {
    e.preventDefault();
    let formObject = new FormData(formEle);
    let response = await postRequest('backend/login.php', formObject);
    if ('error' in response){
        alert(response.error)
        return
    }
    window.location.href = '?page=sleep'
})