.. index:: Kondensator
.. _Kondensator:

Kondensatoren
=============

Ein Kondensator ist ein kleiner Ladungsspeicher. Er besteht im wesentlichen aus
zwei Metallflächen, die sich im Bauteil -- durch einen Isolator voneinander
getrennt -- gegenüber liegen. Kondensatoren stellen somit technische
Verwirklichungen von :ref:`Plattenkondensatoren <gwp:Plattenkondensator>` dar.

Kondensatoren werden in elektrischen Schaltkreisen zu vielerlei Zwecken
eingesetzt: Sie können beispielsweise elektrische Energie zwischenspeichern,
Schwankungen einer Gleichspannung ausgleichen, Frequenzen filtern oder das
Verhalten von Kippschaltungen beeinflussen. Sie sind daher als elementares
Bauteil in fast jeder Schaltung zu finden.

.. _Normaler Kondensator:

"Normale" Kondensatoren
-----------------------

Ohne eine anliegende Spannung verteilen sich die Elektronen im Kondensator
gleichmäßig über die Metallplatten und die Verbindungsleitungen. Liegt an einem
Kondensator eine Gleichspannung an, so fließen kurzzeitig zusätzliche Elektronen
auf die mit dem Minus-Pol verbundene Metallfläche, von der mit dem Plus-Pol
verbundenen Metallfläche werden Elektronen weggezogen -- die Kondensator-Platten
laden sich elektrisch auf.


.. figure::
    ../pics/bauteile/schaltzeichen-kondensator.png
    :name: fig-schaltzeichen-kondensator
    :alt:  fig-schaltzeichen-kondensator
    :align: center
    :width: 30%

    Schaltzeichen eines Kondensators.

    .. only:: html

        :download:`SVG: Schaltzeichen Kondensator
        <../pics/bauteile/schaltzeichen-kondensator.svg>`

Während sich der Kondensator durch den externen Stromfluss auflädt, erhöht sich
die Spannung, die zwischen seinen Metallplatten anliegt -- der Kondensator wird
selbst zu einer kleinen Stromquelle. Allerdings ist die Menge an elektrischer
Ladung, die der Kondensator bei einer anliegenden externen Spannung speichern
kann, begrenzt.

*Definition:*
    Das Verhältnis aus maximal speicherbarer Ladung :math:`Q` bei einer externen
    Spannung :math:`U` wird als Kapazität :math:`C` des Kondensators bezeichnet:

.. math::
    :label: eqn-kapazität

    C = \frac{Q}{U}

*Einheit:*
    Die Kapazität eines Kondensators wird in Farad :math:`(\unit[]{F})` angegeben.

.. math::

    \unit[1]{F} = \frac{\unit[1]{C}}{\unit[1]{V}}

*Beispiele:*

* Ein Kondensator, der durch eine Stromstärke von einem Ampere in einer Sekunde
  auf eine Spannung von einem Volt aufgeladen wird, hat eine Kapazität von einem
  Farad. Eine derartige Kapazitätsmenge ist enorm hoch.

* Die Werte von normalen Folien- und Keramik-Kondensatoren liegen im Bereich
  einiger :math:`\unit[]{pF}`- oder :math:`\unit[]{nF}`, maximal einiger
  :math:`\unit[]{\mu F}`. Der Kapazitätswert ist auf jedem Kondensator mit
  der unten genannten Notation aufgedruckt.

.. math::

    \unit[1]{pF} &= \unit[10 ^{-12}]{F} =
    \unit[\frac{1}{1\,000\,000\,000\,000}]{F} = \unit[0,000\,000\,000\,001]{F}
    \\[4pt]
    \unit[1]{nF} &= \unit[10 ^{-9}]{F} =
    \unit[\frac{1}{1\,000\,000\,000}]{F} = \unit[0,000\,000\,001]{F} \\[4pt]
    \unit[1]{\mu F} &= \unit[10 ^{-6}]{F} =
    \unit[\frac{1}{1\,000\,000}]{F} = \unit[0,000\,001]{F}


.. _Notation von Kondensatorwerten:

.. rubric:: Notation von Kondensatorwerten

Auf jedem Kondensator ist aufgedruckt, welche Kapazität er besitzt und welche
elektrische Spannung maximal an ihm anliegen darf. Die Werte werden -- ähnlich
wie :ref:`Widerstandswerte <Notation von Widerstandswerten>` -- mit folgenden
Besonderheiten angegeben:

1. Der Kapazitätswert eines Kondensators, beispielsweise :math:`\unit[10]{nF}`,
   wird in Schaltplänen und auf Bauteilen oft in Klarschrift angegeben
   (:math:`\unit[10]{n}`, das "F" wird weggelassen). Teilweise findet man den
   Kapazitätswert eines Kondensators jedoch auch in Potenzschreibweise
   (:math:`10^3`) aufgedruckt. Hierbei geben die ersten beiden Ziffern den
   Kondensator-Wert :math:`(10)` und die dritte Ziffer die :ref:`Zehnerpotenz
   <gwp:Zehnerpotenzen>` :math:`( \cdot 10^3)` an. Die Wertangabe bezieht sich
   dabei auf Pikofarad als kleinste Kapazität handelsüblicher Kondensatoren. Es
   gilt:

   .. math::

       \unit[1]{nF} &= \unit[1\,000]{pF} = \unit[1 \cdot 10^3]{pF} \\[4pt]
       \unit[1]{\mu F} &= \unit[1\,000]{nF} = \unit[1 \cdot 10^6]{pF}

2. Ähnlich wie bei Widerständen werden Nachkommastellen stets hinter den
   Potenzfaktor geschrieben; eine Kapazitätsangabe von :math:`2n2` entspricht
   somit einem Kapazitätswert von :math:`\unit[2,2]{nF}`. Auf diese Weise ist
   ausgeschlossen, dass man eine Kommastelle aus Versehen "überlesen" könnte.

3. Nach der Kapazitätsangabe ist auf Kondensatoren meist direkt ein einzelner
   Buchstabe aufgedruckt, der die Toleranzklasse des Kondensators angibt.
   :math:`J` bedeutet beispielsweise eine Toleranz von :math:`\pm 5\%`.

4. Schließlich ist noch der Wert der maximalen Spannung aufgedruckt, die an den
   Kondensator angelegt werden darf (beispielsweise :math:`100` für
   :math:`\unit[100]{Volt}`).


.. _Kondensator im Gleichstromkreis:

.. rubric:: Kondensatoren im Gleichstromkreis

Um einen Kondensator voll aufzuladen, sind meist nur wenige
Sekunden(-Bruchteile) nötig. Die Spannung zwischen den beiden Metallplatten ist
dann gleich der Ladespannung.


.. _Kondensator im Wechselstromkreis:

.. rubric:: Kondensatoren im Wechselstromkreis

Legt man an einen Kondensator eine Wechselspannung an, so fließt wechselnd ein
Lade- bzw. Entladestrom. Ein Kondensator wirkt in einem Wechselstromkreis wie
ein Widerstand.

Während der Auflade-Vorgänge wird elektrische Energie auf den Kondensator
übertragen, die während der Entlade-Vorgänge wieder vom Kondensator abgegeben
wird; im zeitlichen Durchschnitt ist daher der Mittelwert der auftretenden
elektrischen Leistungen an einem (idealen) Kondensator gleich Null. Man spricht
in diesem Zusammenhang auch von "Blindleistung"; den Kondensator bezeichnet man
in einem Wechselstromkreis als "Blindwiderstand" oder "kapazitativen
Scheinwiderstand".

Der kapazitative Scheinwiderstand ist von der Kapazität des
Kondensators und der Frequenz des Wechselstroms abhängig; je größer die
Kapazität :math:`C` und je höher die Frequenz :math:`f` des Wechselstroms ist,
desto, desto niedriger ist der kapazitative Scheinwiderstand des Kondensators:

.. math::

    R _{\rm{C}} = \frac{1}{2 \cdot \pi \cdot f \cdot C} = \frac{1}{\omega \cdot
    C}

Hierbei wird mit :math:`\omega = 2 \cdot \pi \cdot f` die Kreisfrequenz des
Wechselstroms bezeichnet.

..  pi-topologie: | cap -- res -- | cap
..  kondensator:
..  * ladungsspeicher Q = C \cdot U -> C sollte gross sein, um bei einer
..  bestimmten Spannung viel Ladung aufnehmen zu können
..  * filter: Z = 1/(j*omega*C) soll minimal werden -> C gross
.. grösstmöglicher kondensator? wenn ideal, ja. sonst: NEIN!
.. z impedance ("impiedäns")

.. versuch: 7483

.. 23 = 23 pf ; 182 = 18 00 pf = 1,8 nF

.. index::
    single: Kondensator; Trimmkondensator
.. _Trimmkondensator:

Trimmkondensatoren
------------------

Als Trimmkondensator (auch Dreh-Kondensator oder kurz "Drehko" genannt)
bezeichnet man einen Kondensator mit einer einstellbaren Kapazität; diese reicht
von Null bis zum angegebenen Höchstwert.

.. figure::
    ../pics/bauteile/schaltzeichen-kondensator-trimmkondensator.png
    :name: fig-schaltzeichen-drehkondensator
    :alt:  fig-schaltzeichen-drehkondensator
    :align: center
    :width: 30%

    Schaltzeichen eines Drehkondensators.

    .. only:: html

        :download:`SVG: Schaltzeichen Drehkondensator
        <../pics/bauteile/schaltzeichen-kondensator-trimmkondensator.svg>`

Der Kapazitätswert von Drehkondensatoren kann üblicherweise mittels eines
Drehknopfs eingestellt werden. Da sich bei den meisten Drehkondensatoren Luft
zwischen den Kondensatorplatten befindet, liegen die maximalen Kapazitätswerte
meist unter :math:`\unit[500]{pF}`. Derartige Kondensatoren werden
beispielsweise in Radios eingesetzt, um den Empfänger auf verschiedene
Senderfrequenzen einstellen zu können.

.. index::
    single: Kondensator; Elektrolytkondensator
    single: Elektrolyt-Kondensator
.. _Elektrolyt-Kondensator:

Elektrolyt-Kondensatoren
------------------------

Elektrolyt-Kondensatoren ("Elkos") haben meist hohe Kapazitätwerte von etwa
:math:`\unit[0,1]{\mu F}` bis :math:`\unit[1000]{\mu F}`, oder sogar mehr.
Elektrolyt-Kondensatoren sind allerdings polarisiert, d.h. sie besitzen jeweils
einen Plus- und einen Minusanschluß, den man nicht vertauschen darf. Die
Anschlüsse sind deutlich gekennzeichnet, oftmals erkennt man den Pluspol
zusätzlich am längeren Anschlußdraht.

.. figure::
    ../pics/bauteile/schaltzeichen-kondensator-elektrolytkondensator.png
    :name: fig-schaltzeichen-elektrolytkondensator
    :alt:  fig-schaltzeichen-elektrolytkondensator
    :align: center
    :width: 30%

    Schaltzeichen eines Elektrolyt-Kondensators.

    .. only:: html

        :download:`SVG: Schaltzeichen Elektrolyt-Kondensator
        <../pics/bauteile/schaltzeichen-kondensator-elektrolytkondensator.svg>`

