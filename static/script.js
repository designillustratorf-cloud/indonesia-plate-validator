// ======================================================
// Plate Validator Indonesia
// script.js
// ======================================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("Plate Validator Loaded");

    initChartAnimation();

    initTableHover();

    initAutoUppercase();

    initCopyStates();

    initThemeToggle();

});

// ======================================================
// THEME TOGGLE
// ======================================================

function initThemeToggle() {
    const toggleBtn = document.getElementById("themeToggle");
    const themeIcon = document.getElementById("themeIcon");
    
    if (!toggleBtn || !themeIcon) return;

    // Set initial icon based on current theme
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    updateIcon(currentTheme);

    toggleBtn.addEventListener("click", () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        updateIcon(newTheme);
        
        // Dispatch custom event for Chart.js
        window.dispatchEvent(new CustomEvent('themeChanged', { detail: newTheme }));
    });

    function updateIcon(theme) {
        if (theme === 'light') {
            themeIcon.classList.remove('bi-moon-stars-fill');
            themeIcon.classList.add('bi-sun-fill');
            themeIcon.style.color = '#f59e0b'; // Amber for sun
        } else {
            themeIcon.classList.remove('bi-sun-fill');
            themeIcon.classList.add('bi-moon-stars-fill');
            themeIcon.style.color = '#f8fafc'; // White for moon
        }
    }
}


// ======================================================
// AUTO UPPERCASE
// ======================================================

function initAutoUppercase(){

    const input=document.querySelector("input[name='plate']");

    if(!input) return;

    input.addEventListener("input",function(){

        this.value=this.value.toUpperCase();

    });

}


// ======================================================
// TABLE EFFECT
// ======================================================

function initTableHover(){

    const rows=document.querySelectorAll("tbody tr");

    rows.forEach(row=>{

        row.addEventListener("mouseenter",()=>{

            row.style.transition=".2s";

        });

    });

}


// ======================================================
// COPY STATE HISTORY
// ======================================================

function initCopyStates(){

    const states=document.querySelectorAll(".state-box");

    if(states.length===0) return;

    states.forEach(item=>{

        item.style.cursor="pointer";

        item.title="Klik untuk menyalin";

        item.addEventListener("click",()=>{

            navigator.clipboard.writeText(item.innerText);

            item.classList.add("bg-success");

            setTimeout(()=>{

                item.classList.remove("bg-success");

            },600);

        });

    });

}


// ======================================================
// CHART ANIMATION
// ======================================================

function initChartAnimation(){

    const chart=document.getElementById("chartValidation");

    if(!chart) return;

    chart.style.opacity=0;

    setTimeout(()=>{

        chart.style.transition=".8s";

        chart.style.opacity=1;

    },300);

}


// ======================================================
// ALERT AUTO HIDE
// ======================================================

setTimeout(()=>{

    const alerts=document.querySelectorAll(".alert-success");

    alerts.forEach(alert=>{

        alert.style.transition=".5s";

        alert.style.opacity=0;

    });

},5000);


// ======================================================
// SMOOTH SCROLL
// ======================================================

document.querySelectorAll("a[href^='#']").forEach(anchor=>{

    anchor.addEventListener("click",function(e){

        e.preventDefault();

        const target=document.querySelector(this.getAttribute("href"));

        if(target){

            target.scrollIntoView({

                behavior:"smooth"

            });

        }

    });

});


// ======================================================
// CONSOLE INFO
// ======================================================

console.log("--------------------------------");

console.log("Plate Validator Indonesia");

console.log("Regex + DFA");

console.log("--------------------------------");