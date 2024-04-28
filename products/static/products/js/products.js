/* jshint esversion: 8, jquery: true */
const editReviewButtons = document.getElementsByClassName("btn-edit-review");
const reviewText = document.getElementById("review_text");
const reviewRating = document.querySelector("select[name='rating']");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

// Loop through each edit button
for (let button of editReviewButtons) {
    button.addEventListener("click", function(e) {
        const reviewId = e.target.getAttribute("review_id");
        const reviewContainer = document.getElementById(`review${reviewId}`);
        const reviewContent = reviewContainer.querySelector(".review-text").innerText;
        
        // Extract the current rating from the review container
        const reviewCurrentRating = reviewContainer.querySelector(".review-rating").innerText.match(/\d+/)[0];
        reviewText.value = reviewContent; 
        reviewRating.value = reviewCurrentRating; 
        submitButton.innerText = "Update Review";
        
        // Set the action attribute of the form to edit the specific review
        reviewForm.setAttribute("action", `edit_review/${reviewId}/`);
        reviewForm.scrollIntoView({ behavior: 'smooth' });// Scroll smoothly to the review form
    });
}
