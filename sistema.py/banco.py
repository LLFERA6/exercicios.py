import os 
import sqlite3
import sys

def pasta_do_banco():
    '''Descobre a pasta onde o comando esta'''
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

CAMINHO_BANCO = os.path.join(pasta_do_banco(), "alunos.db")

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)

def criar_tabela():
    '''Criar a tabela de alunos se ela nao existir.'''
    conn = conectar()
    conn.execute('''
  Create table if not exists alunos(
    id integer prmary key autoincrement,
    nome text not null,
    nota1 real not null,
    nota2 real not null
    )
    
''')
    conn.commit()
    conn.close()

def inseir_alunos():
    '''Devove uma lista de tuplas: (id, nome, nota1, nota2)'''
    conn = conectar()
    conn.execute(
        'Insert into alunos (nome, nota1, nota2) values (?, ?, ?)',

    )
    conn.commit()
    conn.close()

def listar_alunos():
    '''Lista os alunos cadastrados.'''
    conn = conectar()
    linhas = conn.execute(
        
        'Select id, nome, nota1, nota2 from alunos order by nome'
    ).fetchall()
    conn.close()
    return linhas

def buscar_por_nome(texto):
    '''Busca alunos pelo nome.'''
    conn = conectar()
    linhas = conn.execute(
        'select id, nome, nota1, nota2 from alunos where nome Like ? order by nome', (f"%{texto}%",):
    ).fetchall()
    conn.close()