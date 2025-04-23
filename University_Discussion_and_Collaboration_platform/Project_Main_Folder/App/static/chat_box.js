function showReaction(element) {
    const reaction = element.querySelector('.reaction');
    reaction.style.display = 'block';
}

function hideReaction(element) {
    const reaction = element.querySelector('.reaction');
    reaction.style.display = 'none';
}

function reactToMessage(element) {
    const message = element.parentElement;
    alert(`You reacted to the message: "${message.querySelector('p').textContent}"`);
}