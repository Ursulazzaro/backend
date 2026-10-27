"""Tests de autorización — EJERCICIO.

Los dos primeros son la REFERENCIA (ya completos, pasan). Los cuatro de abajo
tienen `assert False, "TODO..."` y FALLAN a propósito: son tu trabajo en la
Fase 1 de la guía.

Reglas:
  - Un test = un comportamiento. No pruebes todo junto.
  - Pensá el caso de borde (¿rol vacío? ¿scope vacío?).
  - Corré `uv run pytest` después de cada uno hasta verlo verde.
"""

from app.rules import (
    can_change_role,
    can_delete,
    can_edit,
    can_manage_users,
    scope_allows_write,
)

import pytest

# ── Referencia (no tocar) ──────────────────────────────────────────────────

def test_scope_allows_write_con_write():
    # Arrange
    scope = "read write"
    # Act
    resultado = scope_allows_write(scope)
    # Assert
    assert resultado is True


def test_scope_allows_write_solo_read():
    assert scope_allows_write("read") is False


# ── Fase 1 · Completá los TODO ─────────────────────────────────────────────

# def test_can_manage_users_solo_admin():
#   assert can_manage_users("admin") is True
#    assert can_manage_users("viewer") is False

@pytest.mark.parametrize("role, esperado", [
    ("admin", True),
    ("editor", False),
    ("viewer", False),
])
def test_can_delete_por_rol(role, esperado):
    assert can_delete(role) is esperado


def test_can_delete_solo_admin():
    assert can_delete("admin") is True
    assert can_delete("editor") is False


def test_can_edit_dueño_puede():
    assert can_edit(owner_id=5, user_id=5, role="editor") is True


def test_can_edit_editor_no_puede_sobre_ajeno():
    assert can_edit(owner_id=5, user_id=9, role="editor") is False

def test_scope_allows_write_vacio():
    assert scope_allows_write("") is False