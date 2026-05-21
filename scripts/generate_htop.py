#!/usr/bin/env python3
"""Generate animated htop-style SVG for kr3shna GitHub profile."""

import datetime

START_DATE = datetime.date(2023, 12, 19)


def get_uptime():
    delta = datetime.date.today() - START_DATE
    years = delta.days // 365
    days = delta.days % 365
    return f"{years} yrs, {days} days"


def get_ist_timestamps():
    utc = datetime.datetime.now(datetime.timezone.utc)
    ist = utc + datetime.timedelta(hours=5, minutes=30)
    return [
        (ist - datetime.timedelta(seconds=s)).strftime("%H:%M:%S")
        for s in [12, 7, 3, 0]
    ]


def main():
    uptime = get_uptime()
    ts = get_ist_timestamps()

    cpu_states = [
        [(68, "68.3"), (75, "75.1"), (61, "61.8")],
        [(52, "52.1"), (47, "47.8"), (58, "58.3")],
        [(89, "89.7"), (93, "93.2"), (85, "85.4")],
        [(34, "34.5"), (41, "41.2"), (29, "29.8")],
    ]
    cpu_durations = [6, 7, 5, 8]
    cpu_y = [28, 46, 64, 82]

    cpu_xml = ""
    for row in range(4):
        for si in range(3):
            pct, val = cpu_states[row][si]
            filled = round(pct / 100 * 28)
            bars = "|" * filled
            empty = " " * (28 - filled)
            sc = "abc"[si]
            cls = f"c{row}{sc}"
            op = "1" if si == 0 else "0"
            y = cpu_y[row]
            cpu_xml += (
                f'  <text x="20" y="{y}" xml:space="preserve" '
                f'class="{cls}" opacity="{op}">'
                f'<tspan fill="#00f0ff">  {row}</tspan>'
                f'<tspan fill="#484858">[</tspan>'
                f'<tspan fill="#00cc33">{bars}</tspan>'
                f'<tspan fill="#484858">{empty}]</tspan>'
                f'<tspan fill="#c0c0c0"> {val:>5}%</tspan>'
                f"</text>\n"
            )

    mem_f = round(52.5 / 100 * 28)
    swp_f = round(7.5 / 100 * 28)
    mem_bars = "|" * mem_f
    mem_empty = " " * (28 - mem_f)
    swp_bars = "|" * swp_f
    swp_empty = " " * (28 - swp_f)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="850" height="450" viewBox="0 0 850 450">
<defs><style>
text {{ font-family: 'Courier New', Courier, monospace; font-size: 13px; }}
.c0a {{ animation: s0 {cpu_durations[0]}s infinite; }}
.c0b {{ animation: s1 {cpu_durations[0]}s infinite; }}
.c0c {{ animation: s2 {cpu_durations[0]}s infinite; }}
.c1a {{ animation: s0 {cpu_durations[1]}s infinite; }}
.c1b {{ animation: s1 {cpu_durations[1]}s infinite; }}
.c1c {{ animation: s2 {cpu_durations[1]}s infinite; }}
.c2a {{ animation: s0 {cpu_durations[2]}s infinite; }}
.c2b {{ animation: s1 {cpu_durations[2]}s infinite; }}
.c2c {{ animation: s2 {cpu_durations[2]}s infinite; }}
.c3a {{ animation: s0 {cpu_durations[3]}s infinite; }}
.c3b {{ animation: s1 {cpu_durations[3]}s infinite; }}
.c3c {{ animation: s2 {cpu_durations[3]}s infinite; }}
.w0 {{ animation: w0 12s infinite; }}
.w1 {{ animation: w1 12s infinite; }}
.w2 {{ animation: w2 12s infinite; }}
.w3 {{ animation: w3 12s infinite; }}
.blink {{ animation: blink 1s infinite; }}
@keyframes s0 {{ 0%, 33.33% {{ opacity: 1; }} 33.34%, 100% {{ opacity: 0; }} }}
@keyframes s1 {{ 0%, 33.33% {{ opacity: 0; }} 33.34%, 66.66% {{ opacity: 1; }} 66.67%, 100% {{ opacity: 0; }} }}
@keyframes s2 {{ 0%, 66.66% {{ opacity: 0; }} 66.67%, 100% {{ opacity: 1; }} }}
@keyframes w0 {{ 0%, 25% {{ opacity: 1; }} 25.01%, 100% {{ opacity: 0; }} }}
@keyframes w1 {{ 0%, 25% {{ opacity: 0; }} 25.01%, 50% {{ opacity: 1; }} 50.01%, 100% {{ opacity: 0; }} }}
@keyframes w2 {{ 0%, 50% {{ opacity: 0; }} 50.01%, 75% {{ opacity: 1; }} 75.01%, 100% {{ opacity: 0; }} }}
@keyframes w3 {{ 0%, 75% {{ opacity: 0; }} 75.01%, 100% {{ opacity: 1; }} }}
@keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
</style></defs>

<rect width="850" height="410" fill="#0d1117" rx="6"/>

{cpu_xml}
<text x="520" y="28" xml:space="preserve"><tspan fill="#484858">Tasks: </tspan><tspan fill="#c0c0c0">8, 1 running</tspan></text>
<text x="520" y="46" xml:space="preserve"><tspan fill="#484858">Load avg: </tspan><tspan fill="#c0c0c0">3.47 2.89 2.34</tspan></text>
<text x="520" y="64" xml:space="preserve"><tspan fill="#484858">Uptime: </tspan><tspan fill="#00f0ff">{uptime}</tspan></text>

<text x="20" y="100" xml:space="preserve"><tspan fill="#00f0ff">Mem</tspan><tspan fill="#484858">[</tspan><tspan fill="#00cc33">{mem_bars}</tspan><tspan fill="#484858">{mem_empty}]</tspan><tspan fill="#c0c0c0"> 4.2G/8.0G</tspan></text>
<text x="20" y="118" xml:space="preserve"><tspan fill="#00f0ff">Swp</tspan><tspan fill="#484858">[</tspan><tspan fill="#ffd700">{swp_bars}</tspan><tspan fill="#484858">{swp_empty}]</tspan><tspan fill="#c0c0c0"> 0.3G/4.0G</tspan></text>

<text x="20" y="144" xml:space="preserve" fill="#484858">   PID  PROCESS                            CPU%    MEM%   STATUS</text>
<line x1="20" y1="149" x2="700" y2="149" stroke="#484858" stroke-width="0.5" stroke-dasharray="2,2"/>

<text x="20" y="164" xml:space="preserve"><tspan fill="#484858">  1001  </tspan><tspan fill="#c0c0c0">python|js|ts|c|cpp|dart            </tspan><tspan fill="#00ff41">78.3</tspan><tspan fill="#c0c0c0">    35.2   </tspan><tspan fill="#00ff41">RUNNING</tspan></text>
<text x="20" y="182" xml:space="preserve"><tspan fill="#484858">  1337  </tspan><tspan fill="#c0c0c0">langchain|langgraph|rag            </tspan><tspan fill="#ff00aa">87.3</tspan><tspan fill="#c0c0c0">    42.1   </tspan><tspan fill="#00ff41">RUNNING</tspan></text>
<text x="20" y="200" xml:space="preserve"><tspan fill="#484858">  2048  </tspan><tspan fill="#c0c0c0">react|nextjs|react-native|expo    </tspan><tspan fill="#00ff41">64.2</tspan><tspan fill="#c0c0c0">    31.8   </tspan><tspan fill="#00ff41">RUNNING</tspan></text>
<text x="20" y="218" xml:space="preserve"><tspan fill="#484858">  3141  </tspan><tspan fill="#c0c0c0">fastapi|nodejs|express             </tspan><tspan fill="#ffd700">45.7</tspan><tspan fill="#c0c0c0">    22.4   </tspan><tspan fill="#ffd700">LISTENING</tspan></text>
<text x="20" y="236" xml:space="preserve"><tspan fill="#484858">  4096  </tspan><tspan fill="#c0c0c0">docker|aws|gcp|vercel              </tspan><tspan fill="#ffd700">38.1</tspan><tspan fill="#c0c0c0">    28.9   </tspan><tspan fill="#00ff41">RUNNING</tspan></text>
<text x="20" y="254" xml:space="preserve"><tspan fill="#484858">  5000  </tspan><tspan fill="#c0c0c0">pytest|jest|selenium               </tspan><tspan fill="#c0c0c0">23.4</tspan><tspan fill="#c0c0c0">    15.2   </tspan><tspan fill="#ffd700">TESTING</tspan></text>
<text x="20" y="272" xml:space="preserve"><tspan fill="#484858">  5500  </tspan><tspan fill="#c0c0c0">sentry|posthog                     </tspan><tspan fill="#c0c0c0">18.7</tspan><tspan fill="#c0c0c0">    12.1   </tspan><tspan fill="#00f0ff">WATCHING</tspan></text>
<text x="20" y="290" xml:space="preserve"><tspan fill="#484858">  6174  </tspan><tspan fill="#c0c0c0">git|github|gitlab                  </tspan><tspan fill="#c0c0c0">15.3</tspan><tspan fill="#c0c0c0">     9.8   </tspan><tspan fill="#00ff41">TRACKING</tspan></text>

<text x="20" y="316" xml:space="preserve" fill="#484858">-- tail -f /var/log/krishna.log -----------------------------------------------</text>
<text x="20" y="334" xml:space="preserve"><tspan fill="#484858">[{ts[0]}]</tspan><tspan fill="#00ff41"> INFO  </tspan><tspan fill="#c0c0c0">agent.langchain </tspan><tspan fill="#484858">-&gt; invoking tool</tspan></text>
<text x="20" y="352" xml:space="preserve"><tspan fill="#484858">[{ts[1]}]</tspan><tspan fill="#00f0ff"> DEBUG </tspan><tspan fill="#c0c0c0">react-native </tspan><tspan fill="#484858">-&gt; hot reload triggered</tspan></text>
<text x="20" y="370" xml:space="preserve"><tspan fill="#484858">[{ts[2]}]</tspan><tspan fill="#00ff41"> INFO  </tspan><tspan fill="#c0c0c0">gpu.cluster </tspan><tspan fill="#484858">-&gt; H2O coolant flowing</tspan></text>
<text x="20" y="388" xml:space="preserve"><tspan fill="#484858">[{ts[3]}]</tspan><tspan fill="#00ff41"> INFO  </tspan><tspan fill="#c0c0c0">git.commit </tspan><tspan fill="#484858">-&gt; "fix: it works now"</tspan></text>

<text x="20" y="414" xml:space="preserve"><tspan fill="#00f0ff">F1</tspan><tspan fill="#c0c0c0">Help  </tspan><tspan fill="#00f0ff">F2</tspan><tspan fill="#c0c0c0">Setup  </tspan><tspan fill="#00f0ff">F3</tspan><tspan fill="#c0c0c0">Search  </tspan><tspan fill="#00f0ff">F4</tspan><tspan fill="#c0c0c0">Filter  </tspan><tspan fill="#00f0ff">F5</tspan><tspan fill="#c0c0c0">Tree  </tspan><tspan fill="#00f0ff">F6</tspan><tspan fill="#c0c0c0">SortBy</tspan></text>

<text x="20" y="434" xml:space="preserve" class="w0" opacity="1"><tspan fill="#00ff41" class="blink">&#x25CF;</tspan><tspan fill="#484858"> ONLINE  H2O: </tspan><tspan fill="#00f0ff">&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2591;&#x2591;&#x2591;</tspan><tspan fill="#c0c0c0"> 73%  </tspan><tspan fill="#484858">GPU: </tspan><tspan fill="#00f0ff">COOLING</tspan><tspan fill="#484858">  TOKENS: </tspan><tspan fill="#ff00aa">&#x221E;</tspan></text>
<text x="20" y="434" xml:space="preserve" class="w1" opacity="0"><tspan fill="#00ff41" class="blink">&#x25CF;</tspan><tspan fill="#484858"> ONLINE  H2O: </tspan><tspan fill="#00f0ff">&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2591;&#x2591;&#x2591;&#x2591;</tspan><tspan fill="#c0c0c0"> 61%  </tspan><tspan fill="#484858">GPU: </tspan><tspan fill="#ffd700">THIRSTY</tspan><tspan fill="#484858">  TOKENS: </tspan><tspan fill="#ff00aa">&#x221E;</tspan></text>
<text x="20" y="434" xml:space="preserve" class="w2" opacity="0"><tspan fill="#00ff41" class="blink">&#x25CF;</tspan><tspan fill="#484858"> ONLINE  H2O: </tspan><tspan fill="#00f0ff">&#x2593;&#x2593;&#x2593;&#x2593;&#x2591;&#x2591;&#x2591;&#x2591;&#x2591;&#x2591;</tspan><tspan fill="#c0c0c0"> 42%  </tspan><tspan fill="#484858">GPU: </tspan><tspan fill="#ff00aa">REFILL</tspan><tspan fill="#484858">  TOKENS: </tspan><tspan fill="#ff00aa">&#x221E;</tspan></text>
<text x="20" y="434" xml:space="preserve" class="w3" opacity="0"><tspan fill="#00ff41" class="blink">&#x25CF;</tspan><tspan fill="#484858"> ONLINE  H2O: </tspan><tspan fill="#00f0ff">&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2593;&#x2591;</tspan><tspan fill="#c0c0c0"> 91%  </tspan><tspan fill="#484858">GPU: </tspan><tspan fill="#00ff41">HAPPY</tspan><tspan fill="#484858">  TOKENS: </tspan><tspan fill="#ff00aa">&#x221E;</tspan></text>

</svg>"""

    with open("htop.svg", "w") as f:
        f.write(svg)

    print(f"Generated htop.svg | Uptime: {uptime} | Timestamps: {ts}")


if __name__ == "__main__":
    main()
