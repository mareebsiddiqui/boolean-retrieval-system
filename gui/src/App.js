import React, { useState } from 'react';
import './App.css';

function App() {

  const [input, setInput] = useState();
  const [results, setResults] = useState([]);

  function camelize(str) {
    let result = str.replace( /([A-Z])/g, "$1" );
    let finalResult = result.charAt(0).toUpperCase() + result.slice(1);
    return finalResult;
  }

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      fetch('http://localhost:5000?query='+input)
      .then(res => {
        return res.json();
      })
      .then(res_json => {
        setResults(res_json.data);
      })
      .catch(err => {
        console.log(err);
      })
    }
  }

  function renderResults() {
    if(results.length > 0) {
      return results.map((result, i) => {
        console.log(result)
        return (
          <div className="result mb-4">
            <p className="lead text-white">{result.doc_id}. {camelize(result.doc_name)}</p>
            <span className="snippet text-white">...{result.doc_snippet}...</span>
          </div>
        );
      })
    } else {
      return <p className="text-white">No results.</p>
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Short Stories
        </h1>
        <div className="col-lg-8 content">
          <div className="form-floating mb-3">
            <input type="text" className="form-control" id="floatingInput" onKeyDown={handleKeyDown} onChange={e => setInput(e.target.value)} autoFocus />
            <label htmlFor="floatingInput">query</label>
          </div>
          {renderResults()}
        </div>
      </header>
    </div>
  );
}

export default App;
