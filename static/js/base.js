const sidebar = document.querySelector(".sidebar");
const content = document.querySelector(".content");
var touchstartX;
var touchendX;

class base{
    
    base(){};

    moveLeft = () => {
        if(window.innerWidth <= 991){
            sidebar.style.margin = "30px 0px 0px 30px";
            sidebar.style.width = "260px";
        }
    }

    moveRight = () => {
        if(window.innerWidth <= 991) {
            sidebar.style.margin = "30px 0px 0px 245px";
            sidebar.style.width = "7vw";
        }
    }

    getStart = (event) => {
        let touches = event.touches || event.targetTouches || event.changedTouches;

        // Iterate through each touch point
        for (let i = 0; i < touches.length; i++) {
            let touch = touches[i];
            touchstartX = touch.clientX;
        }
        return touchstartX;
    }

    getEnd = (event) => {
        let touches = event.changedTouches || [];
        // Iterate through each touch point
        for (let i = 0; i < touches.length; i++) {
            let touch = touches[i];
            touchendX = touch.clientX;
        }
        return touchendX;
    }

    handleGesure = () => {

        if (touchstartX <= touchendX) {
            sidebar.style.transition = "all 0.3s ease-out";
            this.moveRight();
        }
        else {
            sidebar.style.transition = "all 0.3s ease-in";
            this.moveLeft();
        }
    }
}

const root = new base();

sidebar.addEventListener('touchstart', function(event) {
    root.getStart(event);
});

sidebar.addEventListener('touchend', function(event) {
    root.getEnd(event);
    root.handleGesure();
});