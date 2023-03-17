
import React, { useState, useEffect } from 'react';

const GetRest = () => {
    const [posts, setPosts] = useState([]);
    const test = 'hello'
    useEffect(() => {
        fetch('http://synapse.viewdns.net:8050/api/records/')
            .then((response) => response.json())
            .then((data) => {
                let records = []
                const number = Object.keys(data).length;
                for (let i = number - 9; i < number; i++) {
                    records.push(data[i])
                }
                setPosts(records);

                console.log('out');
                console.log(posts[1].name);
            })
            .catch((err) => {
                console.log(err.message);
            });
    }, []);

    return (
        <div className="hi">
            <p>{JSON.stringify(posts)}</p>
            <p>{test}</p>
        </div>)
}

export default GetRest;