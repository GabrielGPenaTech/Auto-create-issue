#!/usr/bin/env python3
"""
Script para criar backlog completo do App Avançar Frota Corretiva
Projeto: https://github.com/orgs/FARIT-digital/projects/1

Requisitos:
- pip install requests python-dotenv
- Criar arquivo .env com GITHUB_TOKEN=seu_token_aqui
- Ou definir variáveis de ambiente

Autor: Assistente IA
Data: 09/09/2025
"""

import os
import sys
import time
import json
import requests
from typing import Dict, List
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv('config.env')

class GitHubBacklogCreator:
    def __init__(self, token: str, repo_owner: str, repo_name: str):
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        }
        self.created_count = 0
        self.failed_count = 0
        
    def create_issue(self, title: str, body: str, labels: List[str], assignee: str = None) -> bool:
        """Cria uma issue no GitHub"""
        url = f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/issues"
        
        data = {
            "title": title,
            "body": body,
            "labels": labels
        }
        
        if assignee:
            data["assignee"] = assignee
            
        try:
            print(f"🔄 [{self.created_count + 1}/25] Criando: {title[:50]}...")
            
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            
            if response.status_code == 201:
                issue_data = response.json()
                print(f"✅ Issue #{issue_data['number']} criada com sucesso!")
                self.created_count += 1
                return True
            else:
                print(f"❌ Erro {response.status_code}: {response.json().get('message', 'Erro desconhecido')}")
                self.failed_count += 1
                return False
                
        except Exception as e:
            print(f"❌ Erro de conexão: {str(e)}")
            self.failed_count += 1
            return False
    
    def create_all_tasks(self):
        """Cria todas as 25 tasks do backlog"""
        
        print("🚀 Iniciando criação do backlog App Avançar Frota Corretiva...")
        print("📋 Projeto: FARIT Digital")
        print("⏳ Aguarde enquanto as issues são criadas...")
        print("-" * 60)
        
        # Lista de todas as tasks
        tasks = self.get_all_tasks()
        
        for task in tasks:
            success = self.create_issue(
                title=task["title"],
                body=task["body"],
                labels=task["labels"],
                assignee=task.get("assignee")
            )
            
            if success:
                time.sleep(1)  # Evitar rate limiting
            else:
                time.sleep(2)  # Esperar mais se houve erro
        
        # Relatório final
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO FINAL")
        print("=" * 60)
        print(f"✅ Issues criadas: {self.created_count}")
        print(f"❌ Falhas: {self.failed_count}")
        print(f"📈 Taxa de sucesso: {(self.created_count/25)*100:.1f}%")
        
        if self.created_count > 0:
            print(f"\n🔗 Acesse: https://github.com/{self.repo_owner}/{self.repo_name}/issues")
            print("🔗 Projeto: https://github.com/orgs/FARIT-digital/projects/1")
        
        print("\n📋 Próximos passos:")
        print("   1. Acesse o projeto no GitHub")
        print("   2. Organize as issues nas colunas")
        print("   3. Atribua responsáveis")
        print("   4. Configure automações")
        
        return self.created_count == 25

    def get_all_tasks(self) -> List[Dict]:
        """Retorna lista completa de todas as tasks"""
        return [
            # ARQUITETURA E CONFIGURAÇÃO INICIAL ( Exemplo de task )
            {
                "title": "TASK-001: Configuração da Estrutura do Projeto",
                "body": """**📋 Descrição**: Configurar a estrutura inicial do projeto com separação de responsabilidades

                ## 🎯 Objetivos
                - [ ] Configurar repositório Git com estrutura monorepo ou separada
                - [ ] Definir arquitetura de pastas (frontend mobile, backend API)
                - [ ] Configurar ambientes (development, homologação, produção)
                - [ ] Documentar padrões de código e convenções de nomenclatura
                - [ ] Configurar ESLint/Prettier para padronização
                - [ ] Criar README.md inicial com instruções de setup

                ## 📊 Critérios de Aceitação
                - Estrutura de pastas bem definida e documentada
                - Ambientes configurados e funcionais
                - Documentação clara para novos desenvolvedores

                **🏷️ Tipo**: Setup | **⭐ Prioridade**: Alta | **⏱️ Estimativa**: 2-3 dias""",
                "labels": ["setup", "high-priority", "architecture"]
            },
        ]


def main():
    """Função principal"""
    print("🔧 Configurando GitHub Backlog Creator...")
    
    # Configurações - Altere aqui seus dados
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    REPO_OWNER = os.getenv('REPO_OWNER', 'FARIT-digital')  # Padrão: FARIT-digital
    REPO_NAME = os.getenv('REPO_NAME')  # Você deve definir o nome do repositório
    
    # Validações
    if not GITHUB_TOKEN:
        print("❌ ERRO: GITHUB_TOKEN não encontrado!")
        print("📋 Configure sua variável de ambiente ou arquivo .env:")
        print("   export GITHUB_TOKEN=seu_token_aqui")
        print("   ou crie arquivo .env com: GITHUB_TOKEN=seu_token_aqui")
        sys.exit(1)
    
    if not REPO_NAME:
        print("❌ ERRO: REPO_NAME não encontrado!")
        print("📋 Configure sua variável de ambiente:")
        print("   export REPO_NAME=nome-do-seu-repositorio")
        print("   ou crie arquivo .env com: REPO_NAME=nome-do-seu-repositorio")
        sys.exit(1)
    
    print(f"✅ Token configurado")
    print(f"✅ Repositório: {REPO_OWNER}/{REPO_NAME}")
    
    # Criar o backlog
    creator = GitHubBacklogCreator(GITHUB_TOKEN, REPO_OWNER, REPO_NAME)
    
    try:
        success = creator.create_all_tasks()
        if success:
            print("\n🎉 SUCESSO TOTAL!")
        else:
            print("\n⚠️  CONCLUÍDO COM ALGUMAS FALHAS")
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Operação cancelada pelo usuário")
        print(f"📊 Issues criadas até agora: {creator.created_count}")
        
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {str(e)}")
        print(f"📊 Issues criadas até a falha: {creator.created_count}")


if __name__ == "__main__":
    main()