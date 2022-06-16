function clearCalc(event){
    event.preventDefault();
    
    document.getElementById("xDimension").value = '';
    document.getElementById("yDimension").value = '';
    document.getElementById("zDimension").value = '';
    document.getElementById("numOfShapes").value = '2';
    document.getElementById("pricePerFoot").value = '';
    document.getElementById("pricePerShape").value = '';
}

function calcPrice(event){
    event.preventDefault();

    const factor = document.getElementById("shapeFactor").value;
    const x = document.getElementById("xDimension").value;
    const y = document.getElementById("yDimension").value;
    const z = document.getElementById("zDimension").value;
    const num = document.getElementById("numOfShapes").value;
    const calcType = document.querySelector("input[name='calcType']:checked").value;

    if(calcType === 'linear'){
        let pricePerFoot = (((x * y) * factor) / num).toFixed(2);
        let pricePerShape = pricePerFoot * 4;

        document.getElementById("pricePerFoot").value = '$' + pricePerFoot + " /ft"
        document.getElementById("pricePerShape").value = '$' + pricePerShape + " /4 ft"
    } else if(calcType === "other") {
        let pricePerShape = (((x * y * z) * factor * 1.5) / num).toFixed(2);

        document.getElementById("pricePerShape").value = '$' + pricePerShape + " /piece"
    }
}

function radChange(event){
    event.preventDefault();

    const calcType = document.querySelector("input[name='calcType']:checked").value;
    
    if(calcType === "other"){
        document.getElementById("zDimDiv").style = "visibility: visible;"
        document.getElementById("ftPriceDiv").style = "visibility: hidden;"
    } else if(calcType === "linear"){
        document.getElementById("zDimDiv").style = "visibility: hidden;"
        document.getElementById("ftPriceDiv").style = "visibility: visible;"
    }
}

function calcFactor(event){
    event.preventDefault();

    const billetPrice = document.getElementById("billetPrice").value;
    let shapeFactor = (billetPrice / 48 / 96 / 4).toFixed(4);

    document.getElementById("calcFactor").value = shapeFactor;
}

function clearFactorCalc(event){
    event.preventDefault();
    
    document.getElementById("billetPrice").value = "";
    document.getElementById("calcFactor").value = "";
}