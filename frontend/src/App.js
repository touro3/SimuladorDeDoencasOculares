import React, { useState } from 'react';

function App() {
    const [image, setImage] = useState(null);
    const [result, setResult] = useState(null);

    const handleImageChange = (e) => {
        setImage(e.target.files[0]);
    };

    const handleSubmit = async () => {
        const formData = new FormData();
        formData.append('image', image);

        const response = await fetch('/api/simulate', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        setResult(data.prediction);
    };

    return (
        <div>
            <h1>Simulador de Doenças Oculares</h1>
            <input type="file" onChange={handleImageChange} />
            <button onClick={handleSubmit}>Simular</button>
            {result && <div>Resultado: {result}</div>}
        </div>
    );
}

export default App;
