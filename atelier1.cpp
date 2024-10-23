#include <iostream>
#include <vector>
#include <string>
#include <openssl/sha.h> 
#include <iomanip>
#include <sstream>

using namespace std;


string sha256(const string &data) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char*)data.c_str(), data.size(), hash);  //fonction SHA256 d'OpenSSL

    stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    }
    return ss.str();
}

// class noeud
class MerkleNode {    
public:
    string hash;
    MerkleNode *left, *right;

    MerkleNode(const string &data) {
        hash = sha256(data);
        left = right = nullptr;
    }

    MerkleNode(MerkleNode *leftNode, MerkleNode *rightNode) {
        left = leftNode;
        right = rightNode;
        hash = sha256(left->hash + right->hash);
    }
};

class MerkleTree {
public:
    MerkleNode *root;

    MerkleTree(const vector<string> &data) {
        vector<MerkleNode *> nodes;

        for (const auto &datum : data) {
            nodes.push_back(new MerkleNode(datum));
        }

        while (nodes.size() > 1) {
            vector<MerkleNode *> newLevel;
            for (size_t i = 0; i < nodes.size(); i += 2) {
                if (i + 1 < nodes.size()) {
                    newLevel.push_back(new MerkleNode(nodes[i], nodes[i + 1]));
                } else {
                    newLevel.push_back(nodes[i]);
                }
            }
            nodes = newLevel;
        }
        root = nodes[0];
    }

    string getRootHash() {
        return root->hash;
    }
};

int main() {
    vector<string> data = {"Bloc A", "Bloc B", "Bloc C", "Bloc D"};

    MerkleTree tree(data);

    cout << "Le hache racine de l'arbre de Merkle est : " << tree.getRootHash() << endl;

    return 0;
}
