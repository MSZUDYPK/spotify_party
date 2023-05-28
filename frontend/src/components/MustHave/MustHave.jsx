import React, { useState } from "react";
import "./MustHave.css";
import { SearchBar } from "./SearchBar/SearchBar";
import { SearchResultsList } from "./SearchResultsList/SearchResultsList";
import SearchResultHeader from "./SearchResultsList/SearchResultHeader/SearchResultHeader";
import {useNavigate} from "react-router-dom";

export default function MustHave() {
  const [results, setResults] = useState([]);
  const navigate = useNavigate();

  const handleSubmitMustHave = () => {
      navigate("/join/enjoy");
  }

  return (
    <div className="must-have-container">
      <h1>Must-have song:</h1>
      <div className="search-bar-container">
        <SearchBar setResults={setResults} />
      </div>
      <div className="search-results-container">
        <SearchResultHeader />
        {results && results.length > 0 && <SearchResultsList results={results} />}
      </div>
        <button onClick={handleSubmitMustHave}>Submit</button>
    </div>
  );
}
