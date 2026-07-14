import xml.etree.ElementTree as ET

mxfile = ET.Element("mxfile", host="65bd71144e")
diagram = ET.SubElement(mxfile, "diagram", id="infographic", name="Visão Geral Infográfico")
graphModel = ET.SubElement(diagram, "mxGraphModel", dx="1200", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1600", pageHeight="1200", background="#ffffff", math="0", shadow="0")
root = ET.SubElement(graphModel, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")

def add_node(id, text, x, y, w, h, parent="1", style="text;html=1;align=center;verticalAlign=top;resizable=0;points=[];autosize=0;strokeColor=#e2e8f0;fillColor=#f8fafc;rounded=1;whiteSpace=wrap;fontFamily=Helvetica;shadow=1;"):
    cell = ET.SubElement(root, "mxCell", id=id, value=text, style=style, vertex="1", parent=parent)
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), **{"as": "geometry"})

def add_wpp_icon(id, x, y, parent):
    style = "shape=image;image=https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed;"
    cell = ET.SubElement(root, "mxCell", id=id, value="", style=style, vertex="1", parent=parent)
    # Relative coordinates inside the parent if parent != 1 it needs relative="1" in mxGeometry
    geom = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width="32", height="32", **{"as": "geometry"})
    if parent != "1":
        geom.set("relative", "1")

def add_edge(id, source, target, text, style="edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;"):
    cell = ET.SubElement(root, "mxCell", id=id, value=text, style=style, edge="1", parent="1", source=source, target=target)
    ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})

# Title
add_node("title", "<div style='font-size: 56px; font-weight: bold; color: #111111; font-family: Helvetica;'>Business Architecture</div><div style='font-size: 24px; color: #555555;'>Plataforma Imobiliária Multi-Tenant (SaaS)</div>", 400, 20, 800, 100, style="text;html=1;align=center;verticalAlign=middle;strokeColor=none;fillColor=none;")

# Actors (Left side, Web side)
html_visitante = "<div style='padding:15px;'><div style='font-size: 60px;'>🚶</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>Visitante Anônimo</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>Busca Imóveis<br>Gera Comportamento</div></div>"
add_node("visitante", html_visitante, 50, 200, 220, 160)

html_usuario = "<div style='padding:15px;'><div style='font-size: 60px;'>👤</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>Usuário Logado</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>(Cliente/Comprador)<br>Salva Favoritos<br>Alerta de Preços</div></div>"
add_node("usuario_logado", html_usuario, 50, 400, 220, 180)

html_portais = "<div style='padding:15px;'><div style='font-size: 60px;'>🌐</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>Portais Externos</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>Zap, VivaReal<br>Extração de Leads</div></div>"
add_node("portais", html_portais, 50, 620, 220, 160)


# Modules
# Module 1: Portal
html_portal = """<div style='padding: 20px; text-align: left;'>
<div style='font-size: 40px; text-align: center; margin-bottom:10px;'>🖥️</div>
<div style='font-size: 22px; font-weight: bold; color: #0f172a; text-align: center; margin-bottom: 15px;'>Portal Web</div>
<ul style='font-size: 14px; color: #334155; padding-left: 20px; line-height: 1.6; margin:0;'>
<li>Busca e Filtros Inteligentes</li>
<li>PDP (Detalhes do Imóvel 360º)</li>
<li>Área do Cliente (Logado)</li>
<li>Captura de Contatos (CTAs)</li>
<li>Conteúdo (SEO/Blog)</li>
<li>Whitelabel Subdomínios</li>
</ul></div>"""
add_node("portal", html_portal, 350, 250, 280, 280, style="text;html=1;align=left;verticalAlign=top;resizable=0;points=[];autosize=0;strokeColor=#38bdf8;strokeWidth=2;fillColor=#f0f9ff;rounded=1;whiteSpace=wrap;fontFamily=Helvetica;shadow=1;")
add_wpp_icon("wpp_portal", 350 + 280 - 20, 250 - 15, "1") # slightly offset to top right

# Module 2: Leads
html_leads = """<div style='padding: 20px; text-align: left;'>
<div style='font-size: 40px; text-align: center; margin-bottom:10px;'>🧲</div>
<div style='font-size: 22px; font-weight: bold; color: #0f172a; text-align: center; margin-bottom: 15px;'>Gestão de Leads</div>
<ul style='font-size: 14px; color: #334155; padding-left: 20px; line-height: 1.6; margin:0;'>
<li>Omnichannel de Captação</li>
<li>Qualificação e Scoring</li>
<li>Roteamento Customizado</li>
<li>Monitoramento de SLA</li>
<li>Nutrição Básica (Nurturing)</li>
</ul></div>"""
add_node("leads", html_leads, 720, 250, 280, 280, style="text;html=1;align=left;verticalAlign=top;resizable=0;points=[];autosize=0;strokeColor=#818cf8;strokeWidth=2;fillColor=#eef2ff;rounded=1;whiteSpace=wrap;fontFamily=Helvetica;shadow=1;")
add_wpp_icon("wpp_leads", 720 + 280 - 20, 250 - 15, "1")

# Module 3: CRM
html_crm = """<div style='padding: 20px; text-align: left;'>
<div style='font-size: 40px; text-align: center; margin-bottom:10px;'>🤝</div>
<div style='font-size: 22px; font-weight: bold; color: #0f172a; text-align: center; margin-bottom: 15px;'>CRM Interno</div>
<ul style='font-size: 14px; color: #334155; padding-left: 20px; line-height: 1.6; margin:0;'>
<li>Gestão da Carteira 360º</li>
<li>Pipeline/Funil Visual</li>
<li>Gestão de Estoque</li>
<li>Agenda e Follow-up</li>
<li>Workflows de Documentação</li>
<li>Painel de Gestor (Dashboards)</li>
</ul></div>"""
add_node("crm", html_crm, 1090, 250, 280, 280, style="text;html=1;align=left;verticalAlign=top;resizable=0;points=[];autosize=0;strokeColor=#34d399;strokeWidth=2;fillColor=#ecfdf5;rounded=1;whiteSpace=wrap;fontFamily=Helvetica;shadow=1;")
add_wpp_icon("wpp_crm", 1090 + 280 - 20, 250 - 15, "1")


# Module 0: Painel SaaS
html_painel = """<div style='padding: 20px; text-align: left;'>
<div style='font-size: 40px; text-align: center; margin-bottom:10px;'>🏢</div>
<div style='font-size: 22px; font-weight: bold; color: #0f172a; text-align: center; margin-bottom: 15px;'>Visão Multi-Tenant</div>
<ul style='font-size: 14px; color: #334155; padding-left: 20px; line-height: 1.6; margin:0;'>
<li>Gestão de Tenants (SaaS)</li>
<li>Identidade Visual e Whitelabel</li>
<li>Isolamento Total de Dados</li>
<li>Configurações Autônomas</li>
<li>Gestão Integrada de Ramais (Bots)</li>
</ul></div>"""
add_node("painel", html_painel, 720, 700, 280, 280, style="text;html=1;align=left;verticalAlign=top;resizable=0;points=[];autosize=0;strokeColor=#f472b6;strokeWidth=2;fillColor=#fdf2f8;rounded=1;whiteSpace=wrap;fontFamily=Helvetica;shadow=1;")

# Internal Actors
html_corretor = "<div style='padding:15px;'><div style='font-size: 60px;'>👔</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>Corretor de Imóveis</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>Atuação no CRM<br>Gestão da Rotina</div></div>"
add_node("corretor", html_corretor, 1450, 250, 220, 160)

html_gestor = "<div style='padding:15px;'><div style='font-size: 60px;'>📈</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>Admin da Imobiliária</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>Gestor/Broker<br>Acompanha Metas</div></div>"
add_node("gestor", html_gestor, 1450, 450, 220, 160)

html_superadmin = "<div style='padding:15px;'><div style='font-size: 60px;'>🛠️</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>Super Admin</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>Gerencia Plataforma<br>Cria Imobiliárias</div></div>"
add_node("superadmin", html_superadmin, 350, 750, 220, 160)

# External Systems
html_juridico = "<div style='padding:15px;'><div style='font-size: 60px;'>✍️</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>Jurídico / Assinatura</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>Contratos Digitais</div></div>"
add_node("juridico", html_juridico, 1450, 700, 200, 140)

html_erp = "<div style='padding:15px;'><div style='font-size: 60px;'>💰</div><div style='font-size: 18px; font-weight: bold; color: #1e293b; margin-top:10px;'>ERP / Financeiro</div><div style='font-size: 13px; color: #64748b; margin-top: 5px; line-height: 1.4;'>Faturamento Global</div></div>"
add_node("erp", html_erp, 1090, 700, 200, 140)

# Edges Core
add_edge("e_vis_portal", "visitante", "portal", "Navega e Interage")
add_edge("e_usu_portal", "usuario_logado", "portal", "Acessa Área Logada")
add_edge("e_port_leads", "portais", "leads", "Envia Leads (API)")

add_edge("e_portal_leads", "portal", "leads", "Captura de Contatos")
add_edge("e_leads_crm", "leads", "crm", "Roleta / Passagem Bão")

add_edge("e_crm_corretor", "crm", "corretor", "Atua no Funil")
add_edge("e_crm_gestor", "crm", "gestor", "Dashboards")

add_edge("e_crm_portal", "crm", "portal", "Sincroniza Imóveis", style="edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;dashed=1;")

add_edge("e_painel_portal", "painel", "portal", "Injeta Whitelabel", style="edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#f472b6;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;dashed=1;")
add_edge("e_painel_leads", "painel", "leads", "Regras de Roteamento", style="edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#f472b6;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;dashed=1;")
add_edge("e_painel_crm", "painel", "crm", "Isolamento de Dados", style="edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#f472b6;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;dashed=1;")

add_edge("e_sa_painel", "superadmin", "painel", "Gerencia Imobiliárias")

add_edge("e_crm_erp", "crm", "erp", "Faturamento", style="edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;dashed=1;")
add_edge("e_crm_juridico", "crm", "juridico", "Contratos", style="edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;dashed=1;")

# WPP Edges (Green lines)
style_wpp = "edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#22c55e;html=1;fontColor=#16a34a;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;"
add_edge("e_wpp_p_l", "wpp_portal", "wpp_leads", "Inicia Conversa e Injeta Lead", style=style_wpp)
add_edge("e_wpp_l_c", "wpp_leads", "wpp_crm", "Histórico e Qualificação Bot", style=style_wpp)

# Generate XML
ET.indent(mxfile)
xml_str = ET.tostring(mxfile, encoding="unicode")
with open("c:/Users/wladi/source/repos/Imobiliaria/2-Lean Inception/VisaoGeralPlataformaImobiliaria.drawio", "w", encoding="utf-8") as f:
    f.write(xml_str)
