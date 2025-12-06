#include <iostream>
#include <fstream>
// This is the final* version. There was literally 0 need for me to make this. Have fun :3
void createfile(int amount, std::string path){
    std::ofstream file(path);
    
    file << "x = int(input('> '))\n";
    file << "if x == 0:\n   print('even')";


    for(int i = 1; i < int(amount+1); i++){
        std::string statement = "";
        if(i % 2 == 0) {
            file << "\nelif x == " + std::to_string(i) + ":\n  print('even')";}
        else {
            file << "\nelif x == " + std::to_string(i) + ":\n  print('odd')";}
        }
    file.close();
}
int main() {
    createfile(1000000000,"example.py");
    return 0;
}
