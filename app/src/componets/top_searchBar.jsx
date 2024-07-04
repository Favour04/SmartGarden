import React from 'react';
import './top_searchBar.css';

const SearchBar = () => {
    // const [searchTerm, setSearchTerm] = useState('');

    // const handleSearch = (e) => {
    //     setSearchTerm(e.target.value);
    //     console.log(searchTerm);
    // };

    return (
        <div id="cover">
            <div class="tb">
                <div class="td">
                    <input type="text" placeholder="Search" required/>
                </div>
                <div class="td" id="s-cover">
                    <button type="submit">
                        <div></div>
                    </button>
                </div>
                </div>
        </div>
    );
};

export default SearchBar;