import React, { useEffect, useState } from 'react';
import './App.css';
import Highlighter from 'react-highlight-words';

function App() {

  const [docIndex, setDocIndex] = useState({});

  const [input, setInput] = useState();

  const [results, setResults] = useState([]);
  const [searchWords, setSearchWords] = useState([]);

  const [showDocument, setShowDocument] = useState(false);

  const [selectedDocId, setSelectedDocId] = useState();
  const [selectedDoc, setSelectedDoc] = useState({});

  const SERVER_URL = 'http://localhost:5000/';
  // const SERVER_URL = 'http://34.228.23.67:41697/';

  useEffect(() => {
    fetch(`${SERVER_URL}/doc_index`)
    .then(res => res.json())
    .then(res_json => {
      console.log(res_json)
      setDocIndex(res_json);
    });
  }, []);

  function camelize(str) {
    if(str) {
      let result = str.replace( /([A-Z])/g, "$1" );
      let finalResult = result.charAt(0).toUpperCase() + result.slice(1);
      return finalResult;
    }
  }

  function handleKeyDown(event) {
    if (event.key === 'Enter') {
      if(input) {
        fetch(`${SERVER_URL}/query?query=`+input)
        .then(res => res.json())
        .then(res_json => {
          setResults(res_json.results);
          setSearchWords(res_json.search_words);
        })
        .catch(err => {
          console.log(err);
        })
      } else {
        setResults([]);
        setSearchWords([]);
        setShowDocument(false);
        setSelectedDocId();
        setSelectedDoc({});
      }
    }
  }

  useEffect(() => {
    if(selectedDocId) {
      fetch(`${SERVER_URL}/document?doc_id=`+selectedDocId)
      .then(res => res.json())
      .then(res_json => {
        setSelectedDoc(res_json);
      })
      .catch(err => {
        console.log(err);
      })
    }
  }, [selectedDocId]);

  function renderResults() {
    if(results.length > 0) {
      return results.map((result, i) => {
        return (
          <div className="result mb-4">
            <p className="lead text-white" href="#">
              {result.doc_id}.
              <a
                href="#" 
                className="text-white" 
                onClick={(e) => {
                  e.preventDefault()
                  setShowDocument(true);
                  setSelectedDocId(result.doc_id);
                }}>
                  {camelize(docIndex[result.doc_id])}
              </a>
            </p>
            {result.doc_snippet && (
              <span className="snippet text-white">
                <Highlighter
                  searchWords={searchWords}
                  textToHighlight={`...${result.doc_snippet}...`}
                />
              </span>
            )}
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
        <h6 className="text-muted">M. Areeb Siddiqui - k181062</h6>
        <h1 className="display-4">
          Short Stories
        </h1>
        {!showDocument && (
          <div className="col-lg-8 content">
            <div className="form-floating mb-3">
              <input type="text" className="form-control" value={input} id="floatingInput" onKeyDown={handleKeyDown} onChange={e => setInput(e.target.value)} autoFocus />
              <label style={{color: "#282c34"}} htmlFor="floatingInput">query + enter</label>
            </div>
            <hr/>
            {renderResults()}
          </div>
        )}
        {showDocument && selectedDoc.doc_name && (
          <>
            <a className="text-white" href="#" onClick={(e) => {
              e.preventDefault();
              setShowDocument(false);
            }}>Back</a>
            <h3>
              {selectedDoc.doc_name}  
            </h3>
            <div className="col-lg-10 content">
              <p style={{textAlign: "justify"}}>
              <Highlighter
                  searchWords={searchWords}
                  textToHighlight={selectedDoc.doc}
                />
              </p>
            </div>
          </>
        )}
        {showDocument && !selectedDoc.doc_name && (
          <p>Loading..</p>
        )}
      </header>
    </div>
  );
}

export default App;
