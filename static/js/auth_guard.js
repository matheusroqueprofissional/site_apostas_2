console.log("ola")
firebase.auth().onAuthStateChanged(user => {
    if (!user) {
        window.location.href = "/login"
    }
    console.log(user)
})