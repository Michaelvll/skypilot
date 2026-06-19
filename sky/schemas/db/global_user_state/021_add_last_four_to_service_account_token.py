"""Add last_four column to service_account_tokens table.

Revision ID: 021
Revises: 020
Create Date: 2026-06-19

"""
# pylint: disable=invalid-name
from typing import Sequence, Union

import sqlalchemy as sa

from sky.utils.db import db_utils

# revision identifiers, used by Alembic.
revision: str = '021'
down_revision: Union[str, Sequence[str], None] = '020'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Add last_four column to store the last 4 chars of the token.

    The full token is only shown once on creation and otherwise stored as a
    hash, so we persist just the last 4 characters to let the dashboard show a
    non-sensitive hint of which token a row corresponds to. Existing rows
    created before this migration keep a NULL value (rendered as nothing).
    """
    from alembic import op  # pylint: disable=import-outside-toplevel

    with op.get_context().autocommit_block():
        db_utils.add_column_to_table_alembic('service_account_tokens',
                                             'last_four',
                                             sa.Text(),
                                             server_default=None)


def downgrade():
    """No-op for backward compatibility."""
    pass
