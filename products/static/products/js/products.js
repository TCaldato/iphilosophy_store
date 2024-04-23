
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
        reviewText.value = reviewContent; // Set the text of the textarea to the review content
        reviewRating.value = reviewCurrentRating; // Set the value of the rating dropdown to the current rating
        submitButton.innerText = "Update Review"; // Change the text of the submit button to indicate update action
        
        // Set the action attribute of the form to edit the specific review
        reviewForm.setAttribute("action", `edit_review/${reviewId}/`);
        reviewForm.scrollIntoView({ behavior: 'smooth' });// Scroll smoothly to the review form
    });
}
