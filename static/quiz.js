// Function to calculate the score
function calculateScore() {
    // Get all the answers from the quiz
    const answers = document.querySelectorAll('input[type="radio"]:checked');
    let score = 0;
    // Correct answers (assuming the correct answers are A for both questions)
    const correctAnswers = ['A', 'A']; // Adjust based on your quiz questions
    // Loop through the answers and compare with correct answers
    answers.forEach((answer, index) => {
        if (answer.value === correctAnswers[index]) {
            score++;
        }
    });
    // Display the result
    document.getElementById('result').innerText = `You scored ${score} out of ${correctAnswers.length}`;
}
// Function to handle the finish button click
function finishQuiz() {
    calculateScore();   
}