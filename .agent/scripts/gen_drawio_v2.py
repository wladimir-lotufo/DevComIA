import xml.etree.ElementTree as ET

mxfile = ET.Element("mxfile", host="65bd71144e")
diagram = ET.SubElement(mxfile, "diagram", id="infographic", name="Visão Geral Infográfico")
graphModel = ET.SubElement(diagram, "mxGraphModel", dx="1200", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1600", pageHeight="1200", background="#f8fafc", math="0", shadow="0")
root = ET.SubElement(graphModel, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")

def add_node(id, text, x, y, w, h, style=""):
    cell = ET.SubElement(root, "mxCell", id=id, value=text, style=style, vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), **{"as": "geometry"})

def add_wpp_icon(id, x, y):
    style = "shape=image;image=https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed;"
    cell = ET.SubElement(root, "mxCell", id=id, value="", style=style, vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width="36", height="36", **{"as": "geometry"})

def add_edge(id, source, target, text, style="edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;fontFamily=Helvetica;"):
    cell = ET.SubElement(root, "mxCell", id=id, value=text, style=style, edge="1", parent="1", source=source, target=target)
    ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})

# Title
add_node("title", "<div style='font-size: 56px; font-weight: bold; color: #0f172a; font-family: Helvetica;'>Business Architecture</div><div style='font-size: 24px; color: #64748b;'>Plataforma Imobiliária Multi-Tenant (SaaS)</div>", 350, 20, 900, 100, style="text;html=1;align=center;verticalAlign=middle;strokeColor=none;fillColor=none;")

# Styles
style_actor = "text;html=1;align=center;verticalAlign=top;resizable=0;points=[];autosize=0;strokeColor=#cbd5e1;fillColor=#ffffff;rounded=1;whiteSpace=wrap;fontFamily=Helvetica;shadow=1;dashed=0;overflow=hidden;"
style_module = "text;html=1;align=left;verticalAlign=top;resizable=0;points=[];autosize=0;strokeWidth=2;rounded=1;whiteSpace=wrap;fontFamily=Helvetica;shadow=1;overflow=hidden;"

style_m1 = style_module + "strokeColor=#38bdf8;fillColor=#f0f9ff;"
style_m2 = style_module + "strokeColor=#818cf8;fillColor=#eef2ff;"
style_m3 = style_module + "strokeColor=#34d399;fillColor=#ecfdf5;"
style_m0 = style_module + "strokeColor=#f472b6;fillColor=#fdf2f8;"

def box_html(emoji, title, subtitle):
    return f"<div style='box-sizing: border-box; width: 100%; height: 100%; padding: 15px; text-align: center;'><div style='font-size: 50px;'>{emoji}</div><div style='font-size: 16px; font-weight: bold; color: #1e293b; margin-top:10px;'>{title}</div><div style='font-size: 12px; color: #64748b; margin-top: 5px; line-height: 1.4;'>{subtitle}</div></div>"

def mod_html(emoji, title, list_items):
    li_str = "".join([f"<li style='margin-bottom:6px;'>{item}</li>" for item in list_items])
    return f"<div style='box-sizing: border-box; width: 100%; height: 100%; padding: 25px 20px;'><div style='font-size: 40px; text-align: center; margin-bottom:10px;'>{emoji}</div><div style='font-size: 20px; font-weight: bold; color: #0f172a; text-align: center; margin-bottom: 20px;'>{title}</div><ul style='font-size: 14px; color: #334155; padding-left: 20px; line-height: 1.4; margin:0;'>{li_str}</ul></div>"

# Central Modules
add_node("portal", mod_html("🖥️", "Portal Web", ["Busca e Filtros Inteligentes", "PDP (Detalhes do Imóvel 360º)", "Área do Cliente (Logado)", "Captura de Contatos (CTAs)", "Conteúdo (SEO/Blog)", "Whitelabel (Subdomínios)"]), 350, 150, 320, 320, style_m1)

add_node("leads", mod_html("🧲", "Gestão de Leads", ["Omnichannel de Captação", "Qualificação e Scoring", "Roteamento Customizado", "Monitoramento de SLA", "Nutrição Básica (Nurturing)"]), 350, 520, 320, 300, style_m2)

add_node("crm", mod_html("🤝", "CRM Interno", ["Gestão da Carteira 360º", "Pipeline/Funil Visual", "Gestão de Estoque", "Agenda e Follow-up", "Workflows de Documentação", "Painel de Gestor (Dashboards)"]), 800, 200, 320, 320, style_m3)

add_node("painel", mod_html("🏢", "Visão Multi-Tenant", ["Gestão de Tenants (SaaS)", "Identidade Visual e Whitelabel", "Isolamento Total de Dados", "Configurações Autônomas", "Gestão Integrada de Ramais"]), 800, 560, 320, 300, style_m0)

# Actors Left
add_node("visitante", box_html("🚶", "Visitante Anônimo", "Busca Imóveis<br>Gera Comportamento"), 50, 150, 200, 150, style_actor)
add_node("usuario_logado", box_html("👤", "Usuário Logado", "(Cliente/Comprador)<br>Salva Favoritos"), 50, 320, 200, 150, style_actor)
add_node("portais", box_html("🌐", "Portais Externos", "Zap, VivaReal<br>Extração de Leads"), 50, 490, 200, 150, style_actor)

# Actors Right
add_node("corretor", box_html("👔", "Corretor de Imóveis", "Atuação no CRM<br>Gestão da Rotina"), 1250, 200, 200, 150, style_actor)
add_node("gestor", box_html("📈", "Admin da Imobiliária", "Gestor/Broker<br>Acompanha Metas"), 1250, 370, 200, 150, style_actor)
add_node("erp", box_html("💰", "ERP / Financeiro", "Faturamento Global"), 1250, 540, 200, 130, style_actor)
add_node("juridico", box_html("✍️", "Jurídico / Assinatura", "Contratos Digitais"), 1250, 690, 200, 130, style_actor)

add_node("superadmin", box_html("🛠️", "Super Admin", "Gerencia Pataforma<br>Cria Imobiliárias"), 400, 850, 200, 150, style_actor)

# Labels spacing in connections
add_edge("e_vis_portal", "visitante", "portal", "Navega", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;")
add_edge("e_usu_portal", "usuario_logado", "portal", "Área Logada", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;")
add_edge("e_port_leads", "portais", "leads", "Envia Leads (API)", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;")

add_edge("e_portal_leads", "portal", "leads", "Captura de Contatos", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
add_edge("e_leads_crm", "leads", "crm", "Passagem Bastão", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;exitX=1;exitY=0.5;entryX=0;entryY=0.7;")

add_edge("e_crm_portal", "crm", "portal", "Sincroniza Imóveis", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;dashed=1;exitX=0;exitY=0.3;entryX=1;entryY=0.5;")

add_edge("e_painel_portal", "painel", "portal", "Whitelabel", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#f472b6;html=1;fontColor=#475569;fontSize=12;fontStyle=1;dashed=1;exitX=0;exitY=0.25;entryX=1;entryY=0.75;")
add_edge("e_painel_leads", "painel", "leads", "Roteamento", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#f472b6;html=1;fontColor=#475569;fontSize=12;fontStyle=1;dashed=1;exitX=0;exitY=0.75;entryX=1;entryY=0.8;")
add_edge("e_painel_crm", "painel", "crm", "Isolamento de Dados", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#f472b6;html=1;fontColor=#475569;fontSize=12;fontStyle=1;dashed=1;exitX=0.5;exitY=0;entryX=0.5;entryY=1;")
add_edge("e_sa_painel", "superadmin", "painel", "Gere Tenants", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;exitX=1;exitY=0.5;entryX=0;entryY=0.9;")

add_edge("e_crm_corretor", "crm", "corretor", "Atua no Funil", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;exitX=1;exitY=0.2;entryX=0;entryY=0.5;")
add_edge("e_crm_gestor", "crm", "gestor", "Dashboards", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;exitX=1;exitY=0.6;entryX=0;entryY=0.5;")
add_edge("e_crm_erp", "crm", "erp", "Faturamento", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;dashed=1;exitX=1;exitY=0.8;entryX=0;entryY=0.5;")
add_edge("e_crm_juridico", "crm", "juridico", "Contratos", "edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#94a3b8;html=1;fontColor=#475569;fontSize=12;fontStyle=1;dashed=1;exitX=0.75;exitY=1;entryX=0;entryY=0.5;")

# WPP Icons
add_wpp_icon("wpp_portal", 350 + 320 - 25, 150 - 15)
add_wpp_icon("wpp_leads", 350 + 320 - 25, 520 - 15)
add_wpp_icon("wpp_crm", 800 + 320 - 25, 200 - 15)

# WPP Edges
style_wpp = "edgeStyle=curved;endArrow=blockThin;endFill=1;strokeWidth=2;strokeColor=#22c55e;html=1;fontColor=#16a34a;fontSize=12;fontStyle=1;labelBackgroundColor=#ffffff;"
add_edge("e_wpp_p_l", "wpp_portal", "wpp_leads", "Inicia Conversa e Injeta Lead", style_wpp)
add_edge("e_wpp_l_c", "wpp_leads", "wpp_crm", "Histórico e Qualificação Bot", style_wpp)

ET.indent(mxfile)
xml_str = ET.tostring(mxfile, encoding="unicode")
with open("c:/Users/wladi/source/repos/Imobiliaria/2-Lean Inception/VisaoGeralPlataformaImobiliaria.drawio", "w", encoding="utf-8") as f:
    f.write(xml_str)
