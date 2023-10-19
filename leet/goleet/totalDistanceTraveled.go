package main

func DistanceTraveled(mainTank int, additionalTank int) int {
    var (
        totalFuel int = mainTank
        addTank int = additionalTank
        extraFuel int = mainTank
    )
    for extraFuel >= 5 && addTank > 0 {
        leftover := extraFuel % 5
        extraFuel /= 5
        if extraFuel > addTank {
            totalFuel += addTank
            addTank = 0
            break
        }
        totalFuel += extraFuel
        addTank -= extraFuel
        extraFuel += leftover
    }
    return (totalFuel * 10)
}
