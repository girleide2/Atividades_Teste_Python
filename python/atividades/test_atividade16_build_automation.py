import pytest
from unittest.mock import patch
from typing import List
from atividade16_build_automation import AutomationModel, RobotModel, StatusEnum

# Simulando a sessão do banco de dados
class db_context:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def query(self, model):
        # Método fictício para simular consultas ao banco de dados
        return self

    def filter_by(self, **kwargs):
        # Método fictício para simular filtros nas consultas ao banco de dados
        return self

    def first(self):
        # Método fictício para simular a obtenção do primeiro resultado da consulta
        return AutomationModel(id=1, name="Test Automation", status=StatusEnum.RUNNING)

    def all(self):
        # Método fictício para simular a obtenção de todos os resultados da consulta
        return []

    def commit(self):
        pass

def send_to_pack(robot_id):
    pass

def orchestration_create(automation_id):
    pass

@patch('atividade16_build_automation.send_to_pack')
@patch('atividade16_build_automation.orchestration_create')

def test_automation_build(*args, **kwargs):
    automation_id = 1
    with db_context() as session:
        automation: AutomationModel | None = (
            session.query(AutomationModel).filter_by(id=automation_id).first()
        )
        print(f"Automation: {automation}") 
        robots: List[RobotModel | None] = (
            session.query(RobotModel)
            .filter_by(automation_id=automation.id)
            .all()
        )
        print(f"Robots: {robots}")

if __name__ == "__main__":
    pytest.main(["-s", "-x", "test_atividade16_build_automation.py", "-vv"])
