var container = document.getElementById('animate');
//var emoji = ['🍇','🍈','🍉','🍊','🍋','🍌','🍍','🥭','🍎','🍏','🍐','🍑','🍒','🍓','🥝','🍅','🥥','🥑','🍆','🥔','🥕','🌽','🌶','🥒','🥬','🥦','🧄','🧅','🍄','🥜','🌰','🍞','🥐','🥖','🥨','🥯','🥞','🧇','🧀','🍖','🍗','🥩','🥓','🍔','🍟','🍕','🌭','🥪','🌮','🌯','🥙','🧆','🥚','🍳','🥘','🍲','🥣','🥗','🍿','🧈','🧂','🥫','🍱','🍘','🍙','🍚','🍛','🍜','🍝','🍠','🍢','🍣','🍤','🍥','🥮','🍡','🥟','🥠','🥡','🦪','🍦','🍧','🍨','🍩','🍪','🎂','🍰','🧁','🥧','🍫','🍬','🍭','🍮','🍯','🍼','🥛','☕','🍵','🍶','🍾','🍷','🍸','🍹','🍺','🍻','🥂','🥃','🥤','🧃','🧉','🧊','🥢','🍽','🍴','🥄'];
var emoji = ['🌯'];
var circles = [];

for (var i = 0; i < 100; i++) {
    addEmoji(Math.random()*20000, emoji[Math.floor(Math.random() * emoji.length)]);
}

function getRandBetween(min, max) {
  return Math.random() * (max-min) + min
}

function addEmoji(delay, color) {
    setTimeout(function() {
          var c = new Emoji(emoji, {
                  x: -0.15 + Math.random() * 0.3,
                  y: 1 + Math.random() * 1
                });
          circles.push(c);
        }, delay);
}

function Emoji(emoji, v) {
    var _this = this;
    this.x = Math.random() * 1300;
    this.y = Math.random() * 13;
    this.v = v;
    this.element = document.createElement('span');
    
    this.element.innerHTML = emoji;
    this.element.style.fontSize = getRandBetween(12, 70) + 'px';
    this.element.style.position = 'absolute';

    container.appendChild(this.element);

    this.setXPosition = function() {
      _this.x = Math.random() * 1300
    }
  
    this.setYPosition = function() {
      _this.y = Math.random() * 30
    }

    this.update = function() {
          if (_this.y > 1800) {
                  _this.y = Math.random() * 13;
                  _this.x = Math.random() * 1300;
                }
          _this.y += _this.v.y;
          _this.x += _this.v.x;
          this.element.style.transform = 'translate3d(' + _this.x + 'px, ' + _this.y + 'px, 0px)';
          this.element.style.webkitTransform = 'translate3d(' + _this.x + 'px, ' + _this.y + 'px, 0px)';
          this.element.style.mozTransform = 'translate3d(' + _this.x + 'px, ' + _this.y + 'px, 0px)';
        };
}

function animate() {
    for (var i in circles) {
          circles[i].update();
        }
    requestAnimationFrame(animate);
}

animate();
