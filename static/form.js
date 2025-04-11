document.getElementById("nextBtn").addEventListener("click", function () {
    var healthTab = new bootstrap.Tab(document.querySelector('a[href="#health"]'));
    healthTab.show();
});

document.getElementById("nextBtn2").addEventListener("click", function () {
    var healthTab = new bootstrap.Tab(document.querySelector('a[href="#symptoms"]'));
    healthTab.show();
});

// Remove the event listener for the "predict-btn" and the fetch logic.
// The form will now submit traditionally.