#include <iostream>
#include <vector>

using namespace std;

class matrix{
public:
    int size = 3;
    const vector<float> FL, SL, TL, IT;
    //argumentos que são alterados
    vector<float> first_line, second_line, third_line, it, ex_error;
    float x, y, z, error, errorX, errorY, errorZ, deltaX, deltaY, deltaZ;

    matrix(vector<float> f, vector<float> s, vector<float> t, vector<float> it, float error) : FL(f), SL(s), TL(t), IT(it)
    {
        first_line = f;
        second_line = s;
        third_line = t;
        this->it = it;
        this->error = error;
    }

    //Troca as linhas 1 e 2 da matriz
    void matrixSwap1_2() {
        first_line.swap(second_line);
        iter_swap(it.begin(), it.begin() +1);
    }

    //Troca as linhas 1 e 3 da matriz
    void matrixSwap1_3() {
        first_line.swap(third_line);
        iter_swap(it.begin(), it.begin() +2);
    }

    //Neutraliza o primeiro elemento da primeira linha
    void UFirst_line(){
        float f_elem = first_line[0];
        for(size_t i = 0; i < first_line.size(); i++)
        {
            first_line[i] /= f_elem;
        }
        it[0] /= f_elem;
    }

    //Condensa a primeira coluna da matriz (primeiros elementos da segunda e terceira linha passam a 0)
    void firstStep(){
            float n2 = second_line[0] / first_line[0];
            float n3 = third_line[0] / first_line[0];
            for (int i = 0; i < size;i++) {
                second_line[i] -= n2 * first_line[i];
                third_line[i] -= n3 * first_line[i];
            }
            it[1] -= it[0] * n2;
            it[2] -= it[0] * n3;
    }

    //Condensa a segunad coluna da matriz (segundo elemento da terceira linha passa a 0)
    void secondStep(){
        float n3 = third_line[1] / second_line[1];
        for(int i = 1; i < size; i++)
            third_line[i] -= second_line[i] *n3;
        it[2] -= it[1] * n3;
    };


    //Determina as incógnitas após o sistema estar condensado
    void thirdStep(){
        z = it[2] / third_line[2];
        y = (it[1] - z*second_line[2]) / second_line[1];
        x = (it[0] - y*first_line[1] - z*first_line[2]);
    }

    //Resolve a equação: A * erroX = erroB - erroA * X
    void extError()
    {
        vector<float> E(size, error);
        float result;
        result = error - (E[0]*x + E[1]*y + E[2]*z);
        for(int i = 0; i < size; i++)
            ex_error.push_back(result);
    }

    //Resolve o sistema
    void solve()
    {
        deltaX = IT[0] - (x * FL[0] + y * FL[1] + z * FL[2]);
        deltaY = IT[1] - (x * SL[0] + y * SL[1] + z * SL[2]);
        deltaZ = IT[2] - (x * TL[0] + y * TL[1] + z * TL[2]);
    }
};


void Gauss_Method(matrix* sys)
{

    /**
     * Para colocar a primeira linha unitária na primeira posição
     */
    if(sys->first_line[0] != 1){
        if(sys->second_line[0] == 1)
            sys->matrixSwap1_2();
        else if(sys->third_line[0] == 1)
            sys->matrixSwap1_3();
        else
            sys->UFirst_line();
    }

    //1_passo -> subtrair a segunda coluna para zerar o primeiro elemento das duas últimas linhas

    sys->firstStep();

    //2_passo -> subtrair a terceira linha pela segunda

    sys->secondStep();

    //3_passo -> resolver sistema

    sys->thirdStep();

    cout << "SOLUTION:" << endl;
    cout << "X = " << sys->x << endl;
    cout << "Y = " << sys->y << endl;
    cout << "Z = " << sys->z << endl;

    //ESTABILIDADE EXTERNA
    //Função que resolve a equação: A * erroX = erroB - erroA * X

    sys->extError();

    //Repetir o processo inicial, mas desta vez com a matriz dos termos independentes com o erro

    cout << "ESTABILIDADE EXTERNA:" << endl;

    matrix error_ext(sys->FL, sys->SL, sys->TL, sys->ex_error, sys->error);
    if(error_ext.first_line[0] != 1){
        if(error_ext.second_line[0] == 1)
            error_ext.matrixSwap1_2();
        else if(error_ext.third_line[0] == 1)
            error_ext.matrixSwap1_3();
        else
            error_ext.UFirst_line();
    }

    error_ext.firstStep();
    error_ext.secondStep();
    error_ext.thirdStep();

    cout << "ERROR-X: " << error_ext.x << endl;
    cout << "ERROR-Y: " << error_ext.y << endl;
    cout << "ERROR-Z: " << error_ext.z << endl;

    //ESTABILIDADE INTERNA

    cout << "ESTABILIDADE INTERNA:" << endl;

    sys->solve();
    cout << "DELTA-X: " << sys->deltaX << endl;
    cout << "DELTA-Y: " << sys->deltaY << endl;
    cout << "DELTA-Z: " << sys->deltaZ << endl;

}

int main() {

    matrix m_({3,-1,2}, {1,1,1}, {2,0,1}, {-1,8,5}, 0.5);
    Gauss_Method(&m_);

    cout << "############################" << endl;

    matrix m__({7,2,0}, {4, 10, 1}, {5, -2, 8}, {24,27,27}, 0.5);
    Gauss_Method(&m__);

    return 0;
}