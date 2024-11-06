// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


contract MiniSocial {

struct Post{

string msg;
address author;


}



Post [] public  posts;

// notre function

function publishPosts(string memory message ) public {

 posts.push(Post({msg: message, author: msg.sender}));

}

function getPost(uint index) public view returns(string memory, address){


require(index < posts.length, "Index hors des limites");

Post memory post = posts[index];

return (post.msg, post.author);

}

function deletePost(uint index) public {
        require(index < posts.length, "Index hors des limites");
        require(posts[index].author == msg.sender, "Vous pouvez supprimer seulement vos messages");

        // Remplace le post à supprimer par le dernier post
        posts[index] = posts[posts.length - 1];
        
        // Supprime le dernier élément du tableau
        posts.pop();
    }


function getTotalPosts() public view returns (uint) {

return posts.length;

}


}