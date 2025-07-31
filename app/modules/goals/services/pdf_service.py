"""
Wiki Veloz Fibra - PDF Service
Serviço para geração de relatórios PDF das metas

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

import os
import tempfile
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas

from app.modules.goals.models.goal import GoalStatus, GoalType


class PDFService:
    """Serviço para geração de relatórios PDF"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Configura estilos customizados para o PDF"""
        # Título principal
        self.styles.add(ParagraphStyle(
            name='Title',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#1a365d')
        ))
        
        # Subtítulo
        self.styles.add(ParagraphStyle(
            name='Subtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=20,
            textColor=colors.HexColor('#2d3748')
        ))
        
        # Cabeçalho de seção
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading3'],
            fontSize=14,
            spaceAfter=12,
            textColor=colors.HexColor('#4a5568'),
            backColor=colors.HexColor('#f7fafc')
        ))
        
        # Texto normal
        self.styles.add(ParagraphStyle(
            name='NormalText',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=6,
            textColor=colors.HexColor('#2d3748')
        ))
        
        # Texto pequeno
        self.styles.add(ParagraphStyle(
            name='SmallText',
            parent=self.styles['Normal'],
            fontSize=8,
            spaceAfter=4,
            textColor=colors.HexColor('#718096')
        ))
    
    def generate_goals_report(self, goals, summary, generated_by):
        """Gera relatório PDF das metas"""
        # Cria arquivo temporário
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        temp_file.close()
        
        # Cria o documento PDF
        doc = SimpleDocTemplate(
            temp_file.name,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # Lista de elementos do PDF
        story = []
        
        # Cabeçalho
        story.extend(self._create_header(generated_by))
        
        # Resumo executivo
        story.extend(self._create_summary_section(summary))
        
        # Regras de comissão
        story.extend(self._create_commission_rules())
        
        # Lista de metas
        story.extend(self._create_goals_table(goals))
        
        # Rodapé
        story.extend(self._create_footer())
        
        # Gera o PDF
        doc.build(story)
        
        return temp_file.name
    
    def _create_header(self, generated_by):
        """Cria cabeçalho do relatório"""
        elements = []
        
        # Logo e título
        elements.append(Paragraph(
            '<img src="https://via.placeholder.com/100x40/1a365d/ffffff?text=VELOZ+FIBRA" width="100" height="40"/>',
            self.styles['Normal']
        ))
        elements.append(Spacer(1, 20))
        
        elements.append(Paragraph(
            'RELATÓRIO DE METAS E COMISSÕES',
            self.styles['Title']
        ))
        
        elements.append(Paragraph(
            'Sistema de Metas - Veloz Fibra',
            self.styles['Subtitle']
        ))
        
        elements.append(Spacer(1, 20))
        
        # Informações do relatório
        info_data = [
            ['Gerado por:', generated_by],
            ['Data:', datetime.now().strftime('%d/%m/%Y às %H:%M')],
            ['Tipo:', 'Relatório Completo de Metas']
        ]
        
        info_table = Table(info_data, colWidths=[2*inch, 4*inch])
        info_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f7fafc')),
        ]))
        
        elements.append(info_table)
        elements.append(Spacer(1, 30))
        
        return elements
    
    def _create_summary_section(self, summary):
        """Cria seção de resumo executivo"""
        elements = []
        
        elements.append(Paragraph(
            'RESUMO EXECUTIVO',
            self.styles['SectionHeader']
        ))
        
        # Cards de resumo
        summary_data = [
            ['Total de Metas', str(summary['total_goals']), ''],
            ['Concluídas', str(summary['completed_goals']), f"{summary['completion_rate']}%"],
            ['Em Andamento', str(summary['in_progress_goals']), ''],
            ['Atrasadas', str(summary['overdue_goals']), ''],
            ['Progresso Médio', f"{summary['avg_progress']}%", ''],
            ['Faturamento Total', f"R$ {summary['total_revenue']:.2f}", '']
        ]
        
        summary_table = Table(summary_data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch])
        summary_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e2e8f0')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cbd5e0')),
        ]))
        
        elements.append(summary_table)
        elements.append(Spacer(1, 20))
        
        return elements
    
    def _create_commission_rules(self):
        """Cria seção de regras de comissão"""
        elements = []
        
        elements.append(Paragraph(
            'REGRAS DE COMISSÃO - VELOZ FIBRA',
            self.styles['SectionHeader']
        ))
        
        rules_data = [
            ['Tipo de Meta', 'Regra de Cálculo', 'Observações'],
            ['Renovações de Contrato', 'R$ 3,00 por renovação', 'Mínimo 100 renovações'],
            ['Upgrades de Clientes', 'Diferença adicional paga', 'Valor pago a mais'],
            ['Faturamento Total', '5% do faturamento', 'Comissão baseada no faturamento'],
            ['Novos Clientes', 'Metas de quantidade', 'Sem comissão específica'],
            ['Satisfação do Cliente', 'Metas de percentual', 'Sem comissão específica']
        ]
        
        rules_table = Table(rules_data, colWidths=[2*inch, 2*inch, 2*inch])
        rules_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3182ce')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cbd5e0')),
        ]))
        
        elements.append(rules_table)
        elements.append(Spacer(1, 20))
        
        return elements
    
    def _create_goals_table(self, goals):
        """Cria tabela com lista de metas"""
        elements = []
        
        elements.append(Paragraph(
            'LISTA DE METAS',
            self.styles['SectionHeader']
        ))
        
        if not goals:
            elements.append(Paragraph(
                'Nenhuma meta encontrada para exibir.',
                self.styles['NormalText']
            ))
            return elements
        
        # Cabeçalho da tabela
        table_data = [['Título', 'Tipo', 'Status', 'Responsável', 'Progresso', 'Comissão']]
        
        # Dados das metas
        for goal in goals:
            status_text = self._get_status_text(goal.status.value)
            progress_text = f"{goal.progress_percentage:.1f}%"
            commission_text = f"R$ {goal.commission_value:.2f}"
            
            table_data.append([
                goal.title[:30] + ('...' if len(goal.title) > 30 else ''),
                goal.goal_type.value.replace('_', ' ').title(),
                status_text,
                goal.assigned_to[:15] + ('...' if len(goal.assigned_to) > 15 else ''),
                progress_text,
                commission_text
            ])
        
        # Cria tabela
        goals_table = Table(table_data, colWidths=[2*inch, 1.2*inch, 1*inch, 1.2*inch, 0.8*inch, 1*inch])
        goals_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2d3748')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
        ]))
        
        elements.append(goals_table)
        elements.append(Spacer(1, 20))
        
        return elements
    
    def _create_footer(self):
        """Cria rodapé do relatório"""
        elements = []
        
        elements.append(Spacer(1, 30))
        elements.append(Paragraph(
            '---',
            self.styles['SmallText']
        ))
        
        elements.append(Paragraph(
            f'Relatório gerado automaticamente pelo Sistema de Metas da Veloz Fibra<br/>'
            f'Data de geração: {datetime.now().strftime("%d/%m/%Y às %H:%M:%S")}<br/>'
            f'Para dúvidas, entre em contato com a equipe de desenvolvimento.',
            self.styles['SmallText']
        ))
        
        return elements
    
    def _get_status_text(self, status):
        """Converte status para texto legível"""
        status_map = {
            'pending': 'Pendente',
            'in_progress': 'Em Andamento',
            'completed': 'Concluída',
            'cancelled': 'Cancelada'
        }
        return status_map.get(status, status)
    
    def cleanup_temp_file(self, file_path):
        """Remove arquivo temporário"""
        try:
            if os.path.exists(file_path):
                os.unlink(file_path)
        except Exception:
            pass  # Ignora erros de limpeza 